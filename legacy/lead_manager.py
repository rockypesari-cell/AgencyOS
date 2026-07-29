import json
import os

DATABASE_FILE = "database/leads.json"


class LeadManager:
    def __init__(self):
        self.leads = self.load()

    def load(self):
        if not os.path.exists(DATABASE_FILE):
            return []

        with open(DATABASE_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save(self):
        with open(DATABASE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.leads, f, indent=4, ensure_ascii=False)

    def generate_id(self):
        return f"LD-{len(self.leads)+1:04d}"

    def add_lead(self, customer, service, budget, deadline, notes):
        lead = {
            "id": self.generate_id(),
            "customer": customer,
            "service": service,
            "budget": budget,
            "deadline": deadline,
            "status": "New",
            "notes": notes
        }

        self.leads.append(lead)
        self.save()
        return lead

    def get_all(self):
        return self.leads

    def update_status(self, lead_id, status):
        for lead in self.leads:
            if lead["id"] == lead_id:
                lead["status"] = status
                self.save()
                return True
        return False

    def delete(self, lead_id):
        self.leads = [x for x in self.leads if x["id"] != lead_id]
        self.save()

    def search(self, keyword):
        keyword = keyword.lower()
        return [
            lead for lead in self.leads
            if keyword in lead["customer"].lower()
            or keyword in lead["service"].lower()
        ]