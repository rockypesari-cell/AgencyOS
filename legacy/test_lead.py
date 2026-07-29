from lead_manager import LeadManager

lm = LeadManager()

lead = lm.add_lead(
    customer="John Smith",
    service="Logo Design",
    budget="$120",
    deadline="2026-08-01",
    notes="Modern minimalist logo"
)

print(lead)
print(lm.get_all())