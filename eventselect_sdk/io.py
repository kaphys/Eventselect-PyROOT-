import ROOT



def load_tree(file_path, tree_name="mini"):
    file = ROOT.TFile.Open(file_path)
    if not file or file.IsZombie():
        raise IOError(f"Could not open file {file_path}")
    
    tree = file.Get(tree_name)
    if not tree:
        raise KeyError(f"Tree '{tree_name}' not found in {file_path}")
    
    # Keep file alive by attaching it to the tree
    tree._file = file
    
    return tree
