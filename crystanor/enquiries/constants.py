SUCCESSFULLY_FETCHED_ENQUIRY = "Successfully fetched all enquiry"
SUCCESSFULLY_CREATED_ENQUIRY = "Successfully created enquiry"
SUCCESSFULLY_UPDATED_ENQUIRY = "Successfully updated enquiry"
SUCCESSFULLY_DELETED_ENQUIRY = "Successfully deleted enquiry"
NO_DATA_FOUND = "Resource not found"
ADMIN_EMAIL_CONTENT = f"""
            Enquiry Details:

            Name: {{enq.full_name}}
            Email: {{enq.email}}
            Phone: {{enq.phone}}
            Company: {{enq.company_name}}
            Country: {{enq.country}}
            Industry: {{enq.industry}}
            Application: {{enq.application}}
            Purity: {{enq.purity}}
            Volume: {{enq.volume}}
            Packaging: {{enq.packaging}}
            Delivery Terms: {{enq.delivery_terms}}
            Destination Port: {{enq.destination_port}}
            Additional Specs: {{enq.additional_specs}}
        """

USER_EMAIL_CONTENT = f"""
        <html>
        <body style="font-family: Arial; background-color: #f4f4f4; padding: 20px;">
            <div style="background: #ffffff; padding: 20px; border-radius: 10px;">
                
                <h2 style="color: #2c3e50;">Thank You, {{enq_full_name}} 🙌</h2>
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