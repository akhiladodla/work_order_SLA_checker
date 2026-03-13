def get_sla_hours(priority):
    sla={"p1":4,"p2":8,"p3":24,"p4":72}
    return sla.get(priority,-1)
print(get_sla_hours("p1"))
print(get_sla_hours("p2"))
print(get_sla_hours("p3"))
print(get_sla_hours("p4"))
