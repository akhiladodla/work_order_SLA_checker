def get_sla_hours(priority):
    sla={"p1":4,"p2":8,"p3":24,"p4":72}
    return sla.get(priority,-1)
print(get_sla_hours("p1"))
print(get_sla_hours("p2"))
print(get_sla_hours("p3"))
print(get_sla_hours("p4"))
//Here,we need to print the priorities by mentioning p1,p2,p3,p4
//p1,p2,p3,p4 referes the critical,high,medium,low as mentioned in the statement
//it returns the values like 4,8,24,72 if it present in the range,else returns-1
