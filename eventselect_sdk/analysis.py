
import ROOT
import math
import os
from .cuts import apply_selection

def compute_transverse_mass(tree, label="Sample", color=ROOT.kBlue, apply_cuts=True, output_path=None, user_cuts=None):

    hist = ROOT.TH1F(label, f"Transverse Mass ({label}); mT [GeV]; Events", 50, 0, 200)

    

    for event in tree:
        
        if event.lep_n < 2:
            continue
        if apply_cuts:
            if user_cuts:
                if user_cuts.get("lep_n") and event.lep_n < user_cuts["lep_n"]:
                    continue
                if user_cuts.get("met") and event.met_et / 1000.0 < user_cuts["met"]:
                    continue
        else:
            if not apply_selection(event):
                    continue


        pt1 = event.lep_pt[0] / 1000.0
        pt2 = event.lep_pt[1] / 1000.0
        eta1 = event.lep_eta[0]
        eta2 = event.lep_eta[1]
        phi1 = event.lep_phi[0]
        phi2 = event.lep_phi[1]

        met_et = event.met_et / 1000.0
        met_phi = event.met_phi
        met_x = met_et * math.cos(met_phi)
        met_y = met_et * math.sin(met_phi)

        lep1 = ROOT.TLorentzVector()
        lep2 = ROOT.TLorentzVector()
        lep1.SetPtEtaPhiM(pt1, eta1, phi1, 0.0)
        lep2.SetPtEtaPhiM(pt2, eta2, phi2, 0.0)

        dilep = lep1 + lep2
        pt_ll_x = dilep.Px()
        pt_ll_y = dilep.Py()
        pt_ll = dilep.Pt()
        m_ll = dilep.M()
        et_ll = math.sqrt(pt_ll**2 + m_ll**2)

        mt2 = (et_ll + met_et)**2 - (pt_ll_x + met_x)**2 - (pt_ll_y + met_y)**2
        if mt2 > 0:
            hist.Fill(math.sqrt(mt2))

    hist.SetLineColor(color)
    hist.SetLineWidth(2)
    hist.SetStats(False)

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        c = ROOT.TCanvas("c1", "Transverse Mass", 800, 600)
        hist.Draw("HIST")
        c.SaveAs(output_path)
        c.Close()

    return hist


def compare_transverse_mass(signal_tree, background_tree, output_path="plots/mt_comparison.png", apply_cuts=True, user_cuts=None):
    h_sig = compute_transverse_mass(signal_tree, label="Signal", color=ROOT.kRed, apply_cuts=apply_cuts, user_cuts=user_cuts)
    h_bkg = compute_transverse_mass(background_tree, label="Background", color=ROOT.kBlue, apply_cuts=apply_cuts, user_cuts=user_cuts)


    c = ROOT.TCanvas("c_mt", "Signal vs Background", 800, 600)
    h_sig.Draw("HIST")
    h_bkg.Draw("HIST SAME")

    legend = ROOT.TLegend(0.65, 0.75, 0.88, 0.88)
    legend.AddEntry(h_sig, "Signal", "l")
    legend.AddEntry(h_bkg, "Background", "l")
    legend.Draw()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c.SaveAs(output_path)
    c.Close()
