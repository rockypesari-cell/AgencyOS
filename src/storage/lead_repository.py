import json

from src.storage.database import get_connection
from src.domain.lead import Lead


class LeadRepository:
    """
    Handles Lead persistence.
    """

    def save(self, lead: Lead):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO leads
            (
                raw_request,
                service,
                summary,
                priority,
                questions,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                lead.raw_request,
                lead.service,
                lead.summary,
                lead.priority,
                json.dumps(lead.questions),
                lead.created_at.isoformat(),
            ),
        )

        connection.commit()
        connection.close()

    def count(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM leads"
        )

        result = cursor.fetchone()[0]

        connection.close()

        return result

    def get_all(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                raw_request,
                service,
                summary,
                priority,
                questions,
                created_at
            FROM leads
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        connection.close()

        return rows