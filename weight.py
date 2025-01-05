
import usb.core
import usb.util
import time

VENDOR_ID = 0x0922
PRODUCT_ID = 0x8003
MAX_ATTEMPTS = 10
CHIP_WEIGHT = 12
CREDIT_VALUE_SPINS = 5

class Weight():
    def __init__(self):
        self.device = self.find_device()
        self.device_status = True
        self.endpoint = self.device[0][(0,0)][0]
        self.jackpot_weight = 0
        self.tare_weight = self.read_data(self.device, self.endpoint)
        self.credits = 0
        self.ref_chips = 0
        self.tamper = False
        self.stolen = False

    def set_tare_weight(self):
        self.tare_weight = self.read_data(self.device, self.endpoint)

    def set_jackpot_weight(self):
        current_weight = self.read_data(self.device, self.endpoint)
        self.jackpot_weight = current_weight - self.tare_weight
    
    def check_credit(self):
        self.check_device_status()
        if self.device_status == False:
            print("Please Reboot Device.")
            return False
        current_weight = self.read_data(self.device, self.endpoint)
        num_chips = round((current_weight - self.jackpot_weight - self.tare_weight) / CHIP_WEIGHT)
        if num_chips-self.ref_chips > 2:
            print('ERROR: Tampering detected.')
            return False
        if num_chips == self.ref_chips:
            return False
        if num_chips < self.ref_chips:
            print('ERROR: Stolen Chips!')
            return False
        if num_chips > self.ref_chips:
            self.credits += 1
            self.ref_chips = num_chips
            return True
        
    def find_device(self):
        # This function uses PyUSB to look for a weight balance USB device
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            raise ValueError("Device not found")
        if device.is_kernel_driver_active(0):
            device.detach_kernel_driver(0)
        return device

    def check_device_status(self):
        # This function checks the status of the device, if it is still online
        # If the device was offline, it re-configures the device upon reboot
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            self.device_status = False
        elif device and self.device_status:
            self.device_status = True
        elif device and not self.device_status:
            self.device_reboot()
            self.device_status = True

    def device_reboot(self):
        # This function re-configures the device from a reboot
        time.sleep(1)
        self.device = self.find_device()
        self.endpoint = self.device[0][(0,0)][0]
        current_weight = self.read_data(self.device, self.endpoint)
        self.tare_weight = current_weight - self.ref_chips*CHIP_WEIGHT

    def read_data(self, device, endpoint):
        # This function fetches weight data from the device
        attempts = MAX_ATTEMPTS
        while attempts > 0:
            try:
                data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
                grams = data[4] + (256 * data[5])
                #print(str(grams) + "g")
                return grams
            except usb.core.USBError as e:
                device.set_configuration()
                attempts -= 1
                print("Failure! Attempts left:", attempts)

            time.sleep(1)

        print("Failed to connect")

# device = find_device()
# device.set_configuration()
# endpoint = device[0][(0,0)][0]

# while True:
#     read_data(device, endpoint)

weight = Weight()

while True:
    weight.check_credit()
    print(f'Current Credits: {weight.credits}')
    print(f'Current Number of Spins: {weight.credits*CREDIT_VALUE_SPINS}')
    print()
    time.sleep(1)
