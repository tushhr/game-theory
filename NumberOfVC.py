# Let us suppose we will inward "N" type of SKUs, from "M" type of sellers.
# For the sake of simplicity let us suppose one SKU can only be fullfilled by one seller
# We will have a consolidation point (CP) which will bring all these SKUs from all the sellers.
# Now these SKUs needs to move forward to "X" tertiary nodes.
# Since "X" can be a large number (say > 100) for any CP to sort, we will divide these "X" nodes into "Y" clusters
# First we will sort "N" SKUs for "Y" clusters, further which each cluster will sort their SKUs into tertiary nodes.

# Our problem is to efficiently figure out the "Y" so that we can optimise two of our metrics
# Customer Fullfillment Rate: defined as number of orders (out of 100) which were fullfilled correctly.
# Net Quality Detraction: defined as number of people unhappy with the product, again for the ease of algorithm we will ignore the quality of a product, rather only focus on the correctness and missing case of an SKU



# Since supply chain involves human intervention, there's always a chance of manual error.
# Let us consider "A" to be fill rate of sellers, that is out of 100 SKUs seller actually sent us "A" items
# "B" would be the sorting errors of people working on our Conslidation Point, that is out of 100 items a person has to sort (no matter which sorting) they drop "B" items incorrectly.

# "C" is the number of orders per day, and for the sake of simplicity we are assuming one order per customer, where each customer is mapped to one tertiary node 


# To mimic real life scenarios, each order will have at max "P" Unique SKUs and each quantity will be randomly chosen to make sure total SKUs per order restrict us to "Q" items
# To randomize the equation over 100 iterations, each SKUs will be randomly but equally mapped to sellers (This does not represent real life scenarios but for the sake of simplicity we are assuming it)





