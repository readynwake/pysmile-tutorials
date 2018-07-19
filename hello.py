import pysmile
import pysmile_license

def hello_smile():
    net = pysmile.Network()
    #Read XDSL file from disk
    net.read_file("VentureBN.xdsl");

    #Set the evidence on the 'Forecast' node to 'Moderate'
    net.set_evidence("Forecast", "Moderate")
    #Update the network
    net.update_beliefs()

    #Get values(Success, Failure) of Success node
    beliefs = net.get_node_value("Success")
    for i in range(0, len(beliefs)):
        print(net.get_outcome_id("Success", i) + "=" + str(beliefs[i]))

hello_smile()
