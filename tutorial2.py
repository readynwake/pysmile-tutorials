import pysmile

# Tutorial2 loads the XDSL file created by Tutorial1,
# then performs the series of inference calls,
# changing evidence each time.

class Tutorial2:
    def __init__(self):
        print("Starting Tutorial2...")
        net = pysmile.Network()
        
        # load the network created by Tutorial1
        net.read_file("tutorial1.xdsl")
        
        print("Posteriors with no evidence set:")
        net.update_beliefs()
        self.print_all_posteriors(net)
        
        print("Setting Forecast=Good.")
        self.change_evidence_and_update(net, "Forecast", "Good")
        
        print("Adding Economy=Up.")
        self.change_evidence_and_update(net, "Economy", "Up")
        
        print("Changing Forecast to Poor, keeping Economy=Up.")
        self.change_evidence_and_update(net, "Forecast", "Poor")
        
        print("Removing evidence from Economy, keeping Forecast=Poor.")
        self.change_evidence_and_update(net, "Economy", None)
        
        print("Tutorial2 complete.")


    def print_posteriors(self, net, node_handle):
        node_id = net.get_node_id(node_handle)

        #In case of setting evidence on the node, don't print string instead of probablity.
        if net.is_evidence(node_handle):
            print(node_id + " has evidence set (" +
                  net.get_outcome_id(node_handle, 
                                     net.get_evidence(node_handle)) + ")")
        else :
            posteriors = net.get_node_value(node_handle)
            for i in range(0, len(posteriors)):
                print("P(" + node_id + "=" + 
                      net.get_outcome_id(node_handle, i) +
                      ")=" + str(posteriors[i]))

    #Loop in order to print posterior
    def print_all_posteriors(self, net):
        handles = net.get_all_nodes()
        for h in handles:
            self.print_posteriors(net, h)

    def change_evidence_and_update(self, net, node_id, outcome_id):
        #Set evidence
        #if you want to remove evidence, set outcome_id to None
        if outcome_id is not None:
            net.set_evidence(node_id, outcome_id)	
        else:
            net.clear_evidence(node_id)

        #Update contents
        net.update_beliefs()
        self.print_all_posteriors(net)
        print("")
