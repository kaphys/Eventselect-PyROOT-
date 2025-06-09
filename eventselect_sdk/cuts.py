

def apply_selection(event):
    """
    Default event selection logic.
    Modify this function to apply more sophisticated selection cuts.
    """
    if event.lep_n < 2:
        return False

    # Optional: opposite sign same flavor cut
    charge_ok = event.lep_charge[0] * event.lep_charge[1] < 0
    same_flavor = abs(event.lep_type[0]) == abs(event.lep_type[1])
    if not (charge_ok and same_flavor):
        return False

    # MET cut (in GeV)
    if event.met_et / 1000.0 < 30:
        return False

    return True
