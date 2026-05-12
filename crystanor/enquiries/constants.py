SUCCESSFULLY_FETCHED_ENQUIRY = "Successfully fetched all enquiry"
SUCCESSFULLY_CREATED_ENQUIRY = "Successfully created enquiry"
SUCCESSFULLY_UPDATED_ENQUIRY = "Successfully updated enquiry"
SUCCESSFULLY_DELETED_ENQUIRY = "Successfully deleted enquiry"
USER_CONFIRMATION_SUBJECT = "We received your enquiry"
ADMIN_MAIL_SUBJECT = "New Enquiry from {full_name}"
NO_DATA_FOUND = "Resource not found"
FAIL_TO_SEND_ADMIN_NOTIFICATION = "Failed to send admin notification email for enquiry ID: {enquiry_id}"
FAIL_TO_SEND_USER_NOTIFICATION = "Failed to send user confirmation email to: {email}"
ADMIN_EMAIL_CONTENT = """
<html>
<body style="font-family: Arial;">
    <h2>New Enquiry</h2>

    <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
        <tr><td><b>Name</b></td><td>{enq.full_name}</td></tr>
        <tr><td><b>Email</b></td><td>{enq.email}</td></tr>
        <tr><td><b>Phone</b></td><td>{enq.phone}</td></tr>
        <tr><td><b>Company</b></td><td>{enq.company_name}</td></tr>
        <tr><td><b>Country</b></td><td>{enq.country}</td></tr>
        <tr><td><b>Industry</b></td><td>{enq.industry}</td></tr>
        <tr><td><b>Application</b></td><td>{enq.application}</td></tr>
        <tr><td><b>Purity</b></td><td>{enq.purity}</td></tr>
        <tr><td><b>Volume</b></td><td>{enq.volume}</td></tr>
        <tr><td><b>Packaging</b></td><td>{enq.packaging}</td></tr>
        <tr><td><b>Delivery Terms</b></td><td>{enq.delivery_terms}</td></tr>
        <tr><td><b>Destination Port</b></td><td>{enq.destination_port}</td></tr>
        <tr><td><b>Additional Specs</b></td><td>{enq.additional_specs}</td></tr>
    </table>
</body>
</html>
"""

USER_EMAIL_CONTENT = """
        <html>
        <body style="font-family: Arial; background-color: #f4f4f4; padding: 20px;">
            <div style="background: #ffffff; padding: 20px; border-radius: 10px;">
                
                <h2 style="color: #2c3e50;">Thank You, {enq_full_name} 🙌</h2>
                <p>We have received your enquiry successfully.</p>

                <p>Our team will review your request and get back to you shortly.</p>

                <hr>
                
                <p style="margin-top: 20px;">
                    Regards,<br>
                    <strong>Crystanor Team</strong><br>
                </p>
            </div>
        </body>
        </html>
        """
THANKS_FOR_ENQUIRY = "Thank you for your enquiry"