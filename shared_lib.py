# Contains consants that are used by all programs.

from pyeclib.ec_iface import ECDriver

K = 3
M = 13
EC_TYPE = "liberasurecode_rs_vand"
PORT1 = 5005 # sender.py sends to this port, intermediate.py receives from this port.
PORT2 = 6006 # intermediate.py sends to this port, receiver.py receives from this port.

ec_driver = ECDriver(k=K, m=M, ec_type=EC_TYPE)
