SEVERITY_MESSAGES = {
    "LOW": "✅ No immediate security concern detected.",
    "MEDIUM": "⚠️ Suspicious network activity detected.",
    "HIGH": "🚨 High-risk network activity detected.",
    "CRITICAL": "🛑 Critical threat activity detected."
}


def generate_alert(severity, threat_type):
    """Generate a human-readable security alert."""

    message = SEVERITY_MESSAGES.get(
        severity,
        "ℹ️ Unknown threat severity."
    )

    return f"{message} Threat type: {threat_type}"


def get_recommended_action(severity):
    """Return a basic defensive recommendation."""

    actions = {
        "LOW": "Continue monitoring network activity.",
        "MEDIUM": "Review the source and connection pattern.",
        "HIGH": "Investigate the connection and review authentication activity.",
        "CRITICAL": "Investigate immediately and follow your authorized incident-response process."
    }

    return actions.get(
        severity,
        "Review the event manually."
    )


if __name__ == "__main__":
    print(generate_alert("CRITICAL", "dos"))
    print(get_recommended_action("CRITICAL"))
