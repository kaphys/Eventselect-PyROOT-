# cli/eventselect.py
import argparse
from eventselect_sdk.io import load_tree
from eventselect_sdk.analysis import compute_transverse_mass, compare_transverse_mass

parser = argparse.ArgumentParser(description="Eventselect CLI")

subparsers = parser.add_subparsers(dest="command", required=True)

#1.  Subcommand: single plot
plot_parser = subparsers.add_parser("plot", help="Plot transverse mass for a single file")
plot_parser.add_argument("--file", required=True)
plot_parser.add_argument("--label", default="Sample")
plot_parser.add_argument("--output", default="plots/transverse_mass.png")

#2.  Subcommand: compare
parser_compare = subparsers.add_parser("compare", help="Compare signal and background transverse mass")
parser_compare.add_argument("--signal", required=True, help="Signal ROOT file")
parser_compare.add_argument("--background", required=True, help="Background ROOT file")
parser_compare.add_argument("--output", required=True, help="Output image path")

# Optional cut flags
parser_compare.add_argument("--no-cuts", action="store_true", help="Disable all selection cuts")
parser_compare.add_argument("--lep_n", type=int, help="Minimum number of leptons")
parser_compare.add_argument("--met", type=float, help="Minimum MET in GeV")

args = parser.parse_args()

if args.command == "plot":
    tree = load_tree(args.file)
    compute_transverse_mass(tree, label=args.label, output_path=args.output)

elif args.command == "compare":
    # Inside the compare command
    signal_tree = load_tree(args.signal)
    background_tree = load_tree(args.background)

    # Create a dictionary of user-defined cuts
    user_cuts = {
        "lep_n": args.lep_n,
        "met": args.met,
    }

    # Only apply cuts if not disabled
    apply_cuts = not args.no_cuts

    compare_transverse_mass(
        signal_tree,
        background_tree,
        output_path=args.output,
        apply_cuts=apply_cuts,
        user_cuts=user_cuts
    )

