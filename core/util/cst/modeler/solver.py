import time
from core.util.cst.vb import modeler


def add_port(mws, port_name, mode="TE(0,0);TM(0,0)"):
    modeler.solver_add_port(mws.modeler, port_name, mode)


def run(mws):
    isComplete = modeler.run_solver(mws.modeler)
    time.sleep(1)
    mws.save()
    time.sleep(1)
    return isComplete
