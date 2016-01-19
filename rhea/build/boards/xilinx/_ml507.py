
from rhea.build import FPGA
from rhea.build.toolflow import ISE 


class ML507(FPGA):
    vendor = 'xilinx'
    family = 'virtex5'
    device = 'xc5vfx70t'   # 'XC5VFX70T-1CES'
    package = 'ff1136'   # '1FFG1136'
    speed = -1
    _name = 'ml507'
    
    default_clocks = {
        'clock': dict(frequency=100e6, pins=('AH15',)),
    }
    
    default_resets = {
        'reset': dict(active=0, async=True, pins=('E9',)),    
    }
    
    default_ports = {
        'led': dict(pins=('H18', 'L18', 'G15', 'AD26', 'G16', 'AD25', 'AD24', 'AE24')),
                         
        # FX2 connection
        #'fdio': dict(pins=(0, 0, 0, 0, 0, 0, 0, 0)),
        #'addr': dict(pins=(0, 0)),
        #'flaga': dict(pins=(0,)),
        #'flagb': dict(pins=(0,)),
        #'flagc': dict(pins=(0,)),
        #'flagd': dict(pins=(0,)),
    }

    def get_flow(self, top=None):
        return ISE(brd=self, top=top)
