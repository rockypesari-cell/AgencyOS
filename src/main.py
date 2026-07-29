from src.workflows.lead_workflow import LeadWorkflow


def main():
    workflow = LeadWorkflow()

    lead = workflow.execute(
        "I need a modern logo design for an organic coffee brand"
    )

    print(lead)


if __name__ == "__main__":
    main()