from django.core.mail import send_mail
import sendgrid
import os
from sendgrid.helpers.mail import *

_SENDER = "applications@jacobshack.com"
_SUBJECT = "Greetings from jacobsHack!"
_SENDGRID = sendgrid.SendGridAPIClient(apikey="SENDGRID_API_KEY")
_EMAIL_BODY = """Congratulations {},
You have been officially accepted to jacobsHack! Fall 2016. We’d like to
extend you an invitation to join us and 200 other hackers on 15th -16th of
October at Jacobs University in Bremen, Germany.

We would like you to let us know if you can make it to the event or not. If
you’re unable to join for some reason, we can give your spot to other hackers
who would like to attend. RSVP: https://jacobshack.typeform.com/to/b8Lagp
You can also join the event on facebook for more updates.
https://www.facebook.com/events/277473712613843/

Event logistics: Registration opens at 9 AM on 15th October (Saturday) and
the opening ceremony starts at 10.30 AM.

We’ll be sending a Slack invite soon so you can stay in touch with the latest
updates about the event.

If you have any questions, feel free to Email us at hello@jacobshack.com or
message us on Facebook and Twitter.

If you applied for travel reimbursements, please fill out the following form
within the next 3 days.
https://jacobshack.typeform.com/to/oO2rP1

Looking forward to see you in Bremen!

Cheers,
The jacobsHack! team"""
_EMAIL_HTML = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <!--[if gte mso 9]><xml>
     <o:OfficeDocumentSettings>
      <o:AllowPNG/>
      <o:PixelsPerInch>96</o:PixelsPerInch>
     </o:OfficeDocumentSettings>
    </xml><![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="X-UA-Compatible" content="IE=9; IE=8; IE=7; IE=EDGE">
    <title>jacobsHack! 2016</title>
    <!--[if !mso]><!- - -->
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro"
          rel="stylesheet" type="text/css">
    <!--<![endif]-->

</head>
<body style="width: 100% !important;min-width: 100%;-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100% !important;margin: 0;padding: 0;background-color: #FFFFFF">

<style id="media-query">
    /* Client-specific Styles & Reset */
    #outlook a {
        padding: 0;
    }

    /* .ExternalClass applies to Outlook.com (the artist formerly known as Hotmail) */
    .ExternalClass {
        width: 100%;
    }

    .ExternalClass,
    .ExternalClass p,
    .ExternalClass span,
    .ExternalClass font,
    .ExternalClass td,
    .ExternalClass div {
        line-height: 100%;
    }

    #backgroundTable {
        margin: 0;
        padding: 0;
        width: 100% !important;
        line-height: 100% !important;
    }

    /* Buttons */
    .button a {
        display: inline-block;
        text-decoration: none;
        -webkit-text-size-adjust: none;
        text-align: center;
    }

    .button a div {
        text-align: center !important;
    }

    /* Outlook First */
    body.outlook p {
        display: inline !important;
    }

    /*  Media Queries */
    @media only screen and (max-width: 500px) {
        table[class="body"] img {
            height: auto !important;
            width: 100% !important;
        }

        table[class="body"] img.fullwidth {
            max-width: 100% !important;
        }

        table[class="body"] center {
            min-width: 0 !important;
        }

        table[class="body"] .container {
            width: 95% !important;
        }

        table[class="body"] .row {
            width: 100% !important;
            display: block !important;
        }

        table[class="body"] .wrapper {
            display: block !important;
            padding-right: 0 !important;
        }

        table[class="body"] .columns, table[class="body"] .column {
            table-layout: fixed !important;
            float: none !important;
            width: 100% !important;
            padding-right: 0px !important;
            padding-left: 0px !important;
            display: block !important;
        }

        table[class="body"] .wrapper.first .columns, table[class="body"] .wrapper.first .column {
            display: table !important;
        }

        table[class="body"] table.columns td, table[class="body"] table.column td, .col {
            width: 100% !important;
        }

        table[class="body"] table.columns td.expander {
            width: 1px !important;
        }

        table[class="body"] .right-text-pad, table[class="body"] .text-pad-right {
            padding-left: 10px !important;
        }

        table[class="body"] .left-text-pad, table[class="body"] .text-pad-left {
            padding-right: 10px !important;
        }

        table[class="body"] .hide-for-small, table[class="body"] .show-for-desktop {
            display: none !important;
        }

        table[class="body"] .show-for-small, table[class="body"] .hide-for-desktop {
            display: inherit !important;
        }

        .mixed-two-up .col {
            width: 100% !important;
        }
    }

    @media screen and (max-width: 500px) {
        div[class="col"] {
            width: 100% !important;
        }
    }

    @media screen and (min-width: 501px) {
        table[class="container"] {
            width: 500px !important;
        }
    }
</style>
<table class="body"
       style="border-spacing: 0;border-collapse: collapse;vertical-align: top;height: 100%;width: 100%;table-layout: fixed"
       cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
    <tr style="vertical-align: top">
        <td class="center"
            style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;text-align: center;background-color: #FFFFFF"
            align="center" valign="top">

            <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top;background-color: #D9D9D9"
                   cellpadding="0" cellspacing="0" align="center" width="100%"
                   border="0">
                <tbody>
                <tr style="vertical-align: top">
                    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                        width="100%">
                        <!--[if gte mso 9]>
                    <table id="outlookholder" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td>
                    <![endif]-->
                        <!--[if (IE)]>
                    <table width="500" align="center" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                            <td>
                    <![endif]-->
                        <table class="container"
                               style="border-spacing: 0;border-collapse: collapse;vertical-align: top;max-width: 500px;margin: 0 auto;text-align: inherit"
                               cellpadding="0" cellspacing="0" align="center"
                               width="100%" border="0">
                            <tbody>
                            <tr style="vertical-align: top">
                                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                                    width="100%">
                                    <table class="block-grid"
                                           style="border-spacing: 0;border-collapse: collapse;vertical-align: top;width: 100%;max-width: 500px;color: #333;background-color: transparent"
                                           cellpadding="0" cellspacing="0"
                                           width="100%" bgcolor="transparent">
                                        <tbody>
                                        <tr style="vertical-align: top">
                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;text-align: center;font-size: 0">
                                                <!--[if (gte mso 9)|(IE)]><table width="100%" align="center" bgcolor="transparent" cellpadding="0" cellspacing="0" border="0"><tr>
                                                <![endif]-->
                                                <!--[if (gte mso 9)|(IE)]><td valign="top" width="500">
                                                <![endif]-->
                                                <div class="col num12"
                                                     style="display: inline-block;vertical-align: top;width: 100%">
                                                    <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                           cellpadding="0"
                                                           cellspacing="0"
                                                           align="center"
                                                           width="100%"
                                                           border="0">
                                                        <tbody>
                                                        <tr style="vertical-align: top">
                                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;background-color: transparent;padding-top: 20px;padding-right: 0px;padding-bottom: 20px;padding-left: 0px;border-top: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-left: 0px solid transparent">
                                                                <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                                       cellpadding="0"
                                                                       cellspacing="0"
                                                                       width="100%">
                                                                    <tbody>
                                                                    <tr style="vertical-align: top">
                                                                        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-top: 10px;padding-right: 10px;padding-bottom: 0px;padding-left: 10px">
                                                                            <div style="color:#555555;line-height:120%;font-family:'Source Sans Pro', Tahoma, Verdana, Segoe, sans-serif;">
                                                                                <div style="font-size:12px;line-height:14px;color:#555555;font-family:'Source Sans Pro', Tahoma, Verdana, Segoe, sans-serif;text-align:left;">
                                                                                    <p style="margin: 0;font-size: 18px;line-height: 22px;text-align: center">
                                                                                        <span style="font-size: 22px; line-height: 26px;"><strong><span
                                                                                                style="line-height: 26px; font-size: 22px;">Greetings from jacobsHack!</span></strong></span>
                                                                                    </p>
                                                                                </div>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody>
                                                                </table>
                                                                <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                                       cellpadding="0"
                                                                       cellspacing="0"
                                                                       width="100%">
                                                                    <tbody>
                                                                    <tr style="vertical-align: top">
                                                                        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-top: 5px;padding-right: 10px;padding-bottom: 10px;padding-left: 10px">
                                                                            <div style="color:#888888;line-height:120%;font-family:'Source Sans Pro', Tahoma, Verdana, Segoe, sans-serif;">
                                                                                <div style="font-size:12px;line-height:14px;color:#888888;font-family:'Source Sans Pro', Tahoma, Verdana, Segoe, sans-serif;text-align:left;">
                                                                                    <p style="margin: 0;font-size: 14px;line-height: 17px">
                                                                                        Congratulations!
                                                                                        You've
                                                                                        been
                                                                                        officially
                                                                                        accepted
                                                                                        for
                                                                                        jacobsHack!
                                                                                        Fall
                                                                                        2016</p>
                                                                                </div>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <!--[if (gte mso 9)|(IE)]></td>
                                                <![endif]-->
                                                <!--[if (gte mso 9)|(IE)]></td></tr></table>
                                                <![endif]--></td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        <!--[if mso]>
                    </td></tr></table>
                    <![endif]-->
                        <!--[if (IE)]>
                    </td></tr></table>
                    <![endif]-->
                    </td>
                </tr>
                </tbody>
            </table>
            <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top;background-color: #EDEDED"
                   cellpadding="0" cellspacing="0" align="center" width="100%"
                   border="0">
                <tbody>
                <tr style="vertical-align: top">
                    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                        width="100%">
                        <!--[if gte mso 9]>
                    <table id="outlookholder" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td>
                    <![endif]-->
                        <!--[if (IE)]>
                    <table width="500" align="center" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                            <td>
                    <![endif]-->
                        <table class="container"
                               style="border-spacing: 0;border-collapse: collapse;vertical-align: top;max-width: 500px;margin: 0 auto;text-align: inherit"
                               cellpadding="0" cellspacing="0" align="center"
                               width="100%" border="0">
                            <tbody>
                            <tr style="vertical-align: top">
                                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                                    width="100%">
                                    <table class="block-grid"
                                           style="border-spacing: 0;border-collapse: collapse;vertical-align: top;width: 100%;max-width: 500px;color: #000000;background-color: transparent"
                                           cellpadding="0" cellspacing="0"
                                           width="100%" bgcolor="transparent">
                                        <tbody>
                                        <tr style="vertical-align: top">
                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;text-align: center;font-size: 0">
                                                <!--[if (gte mso 9)|(IE)]><table width="100%" align="center" bgcolor="transparent" cellpadding="0" cellspacing="0" border="0"><tr>
                                                <![endif]-->
                                                <!--[if (gte mso 9)|(IE)]><td valign="top" width="500">
                                                <![endif]-->
                                                <div class="col num12"
                                                     style="display: inline-block;vertical-align: top;width: 100%">
                                                    <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                           cellpadding="0"
                                                           cellspacing="0"
                                                           align="center"
                                                           width="100%"
                                                           border="0">
                                                        <tbody>
                                                        <tr style="vertical-align: top">
                                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;background-color: transparent;padding-top: 10px;padding-right: 10px;padding-bottom: 10px;padding-left: 10px;border-top: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-left: 0px solid transparent">
                                                                <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                                       cellpadding="0"
                                                                       cellspacing="0"
                                                                       width="100%"
                                                                       border="0">
                                                                    <tbody>
                                                                    <tr style="vertical-align: top">
                                                                        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;width: 100%;padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px"
                                                                            align="center">
                                                                            <div style="font-size:12px"
                                                                                 align="center">
                                                                                <a href="https://jacobshack.com"
                                                                                   target="_blank">
                                                                                    <img class="center fullwidth"
                                                                                         style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block;border: none;height: auto;line-height: 100%;margin: 0 auto;float: none;width: 100% !important;max-width: 480px"
                                                                                         align="center"
                                                                                         border="0"
                                                                                         src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABG4AAALQCAYAAADB3TZVAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAZbpJREFUeNrs3b9yG8faOOi25CqGP54rOPAVmM420yhg1Waiwo1EXYGl8FcMRAaIJYUbCb4CUdluIdDoCgxdgfFdwcHJFoHsxYgDEpRICiRnprtnnqcKRZ/vs/Hn7Zme6Xe63w4BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgC38JAQAAHna2T8arf4Uq1e5nI7nIgIA/fOzEAAApG9n/2g3nCVp9lavR/Xf3fr//S8RAoB+krgBAEjQzv5RES4naUbX/Kuny+l4IWIA0E8SNwAAke3sH1WJmc0kzd4t/vMPIggA/SVxAwDQobouzWaiprjnW56KKgD0l8QNAEBL6ro0VYKmWL1+DTcvebqLiWVSANBvEjcAAA2plzwV4SJJs9fyR1omBQA9ZztwAIA72NiKe52kKTr+CovldGw3KQDoOTNuAAB+4JslT99uxR2L2jYAMAASNwAA37jFVtwxvdVSANB/lkoBAIO2sRV3teSpCO3XpWnCfDkd/6L1AKD/zLgBAAajha24Y7FMCgAGQuIGAOilDrbijukPLQwAwyBxAwD0QoStuGOZLafjmRYHgGGQuAEAsrOx5GldPLgY0M832wYABkTiBgBIWqJbccekvg0ADIjEDQCQrJ39o8PVn3cica5aJjUXBgAYjgdCAAAk7JkQXPJWCABgWCRuAIAk1XVsCpG4xDIpABgYiRsAIFUHQnDJ6XI6XggDAAyLxA0AkKrfheCSD0IAAMPzkxAAAKnZ2T+qdo76UyTOLZbT8b+EAQCGx4wbACBFZttcprYNAAyUxA0AkCL1bS6zTAoABkriBgBIys7+0eHqz65InKuWSZlxAwADJXEDAKTmiRBcMhECABguiRsAIBk7+0ejYJnUt/4QAgAYLokbACAlkjaXzZfT8UwYAGC4JG4AgJQ8E4JLzLYBgIGTuAEAkrCzf7S3+rMnEpdMhAAAhk3iBgBIhdk2l82W0/FcGABg2CRuAIBUHArBJZZJAQASNwBAfDv7R1VR4l2RuORUCAAAiRsAIAWWSV12apkUAFCRuAEAotrZP6pm2tgG/LIPQgAAVCRuAIDYDoXgO5ZJAQBfSdwAALFZJnVZtUxqIQwAQEXiBgCIZmf/aG/1Z08kLrGbFABwTuIGAIjJbJvLFsvp2DIpAOCcxA0AEJOixJdJ2gAAl0jcAABR7OwfVUmbkUhcYpkUAHCJxA0AEMsTIbhkvpyOS2EAADZJ3AAAndvZP9oNtgH/lmVSAMB3JG4AgBjUtvmeZVIAwHckbgCAGH4XgkuqZVIzYQAAviVxAwB0amf/aLT6sycSl7wVAgDgKhI3AEDXzLb5nvo2AMCVJG4AgK6pb3PZbDkdz4UBALiKxA0A0Jmd/aNi9WckEpdYJgUAXEviBgDo0jMh+I5lUgDAtSRuAIBO7Owf7QbLpL51upyOF8IAAFxH4gYA6EqVtNkVhks+CAEAcBOJGwCgK5ZJXVbNtLFMCgC4kcQNANC6nf2j0epPIRKXWCYFAPyQxA0A0IVDIfiOZVIAwA9J3AAAXbBM6rLFcjq2TAoA+CGJGwCgVTv7R3urPyORuETSBgDYisQNANC234XgO2+FAADYhsQNANC2AyG4ZL6cjmfCAABsQ+IGAGjNzv7R4erPrkhcYpkUALA1iRsAoE1PhOA7lkkBAFv7SQgAgDbs7B+NVn/+EolLZsvp+DdhAAC2ZcYNANAWtW2+94cQAAC3IXEDALTFblLfU98GALgViRsAoHE7+0d7qz8jkbikXE7Hc2EAAG5D4gYAaIPZNt9rdZnUzv5RUdcVAgB65GchAABaoL7N9xpbJlUnaKpZTY/qv0X9/1L4GAB6RuIGAGjUzv5RlbTZFYlLTpfT8eIeMV0nZ36t/46u+NcWq8+YCTUA9IvEDQDQtGdC8J2tl0nt7B9VSa8iXMyoKbb8T0thBoD+kbgBABpTJx0sk7qsmglzekPMqgTNZpJmdMfP+STUANA/EjcAQJMOheA750mbOrG1Xva0rk+z2/TnAAD9IXEDADTJMqkr7OwfvQ4Xy5/aMLfVOAD0k8QNANCIjSU/XHbYwWeUwgwA/fRACACAhphtE4/6NgDQUxI3AEBTDoUgGvVtAKCnJG4AgHvb2T+qdpLaFYkoZsvpeCEMANBPEjcAQBOeCEE0pRAAQH9J3AAA91JvcX0oEtGobwMAPSZxAwDc14EQxLOcjtW3AYAek7gBAO7rdyGIphQCAOg3iRsA4M529o9Gqz97IhGNZVIA0HMSNwDAfZhtE5dlUgDQcxI3AMB9qG8Tz2I5Hc+EAQD6TeIGALiTnf2jKmkzEoloSiEAgP77WQgA4nnw8GE18H2yehUGwLTs+d9fvkwafs8nwhrVh4b7o6pW0Z/CSgvm4SzR+GHVD1neB3BLEjcAEawGSMXqz7sgWUM3FqHhWig7+0e7qz+HQhtV2fD7WfZGW0Z1f3G4uv7Nw1kiuRQWgC3HDkIA0HHH+/Dh69Wfj0HShu6crgZJC4P8Xpkvp+N5w+/5SFjpQHXt+1hfCwHYZvwgBAAddroPH1azbF6IBB37o4X3fCasUZUtvGchrHToRX1NBOBHYwghAOiowz17ungoEnRs3vSShJ39o5FBfnRN17cxg4oYDs28AdjiOi0EAB10tmc1bcy0IYY2ZtscCmt0ZcPvZ5kUsbyor5EAXDeWEAKATpgOTiyTFt7TMqm4ZsvpuOmaRQbOuEYCJEriBqDtjvZsCcJIJIig/PvLl3mTb7izf1Q4nuO3a8N9VLVD2J6wEtHIcj2AG67VQgDQuidCQCSKEvfTh4bfz4AZ10qAhEncALSvEAIiOW3yzXb2j3YN8uNbTsdlw2+pvg2ulQAJk7gBaN9ICIhg8veXL03XQamSNrtCG1VpwIxrJcCwSNwAQD99aOE9LWXoWbs+ePhwZMAMAGmTuAGA/pn//eVL08ukqsG9ZVLxlQ2/nzYFgMRJ3ABA/5y28J4G+PEtltPxrOH3VN8GABIncQMA/fO2hff8XVijayMhVwgrAKTtZyEAgF6Z/f3ly7zJN9zZP9oL3dVBmdWvz/Xf16vXnmb96lOTb/bg4cMqropNA0DiJG4AoF/aKErc1mybS0mab7e5rrcfl7S5UDb8fpa/AUAGJG4AwOC+iwH+jUmaaxSa89x8FbN5w++pvg0AZEDiBgD6pdHitTv7R4fh9stp5uEiSVNumaS5iu3HLzRa3+bBw4dVmxbCCgDpk7gBgB75+8uXRcNv+aPkyTxsJGnC2Wyapr5DoUXPfWr4/cQWADIhcQMAXGln/2gULi+Tmof2kjRXffZIK5wrG34/y6QAIBMSNwBgcH+dajnNSWg5SXONQnOeayP24gsAmZC4AcjPy9BwHRO4ynI6nkU81swIudDGTmEvhZU7+igEAN2SuAHIz+zvL19KYaDnbFV9ofHzXR/CXT14+FAQALrue4UAAEjJzv7RXrj9Tla9dY9duQCAHpC4AQBSUwjBuVMhAIBhk7gBAFKjvs2FT0IAAMMmcQMApKYQgnOlEADAsEncAADJ2Nk/KoL6NmuLemcvAGDAJG4AgJQUQnBOfRsAQOIGAEiK+jYX1LcBACRuAICkFEJwrhQCAEDiBgBIws7+0YEonJstp+O5MAAAEjcAQCosk7pQCgEAUJG4AQBSUQjBOfVtAICvJG4AgOh29o+qLcD3ROJcKQQAQEXiBgBIQSEE58rldLwQBgCgInEDAKTgiRCcs0wKADgncQMApKAQgnOlEAAAaxI3AEBUO/tHo9WfkUh8tVhOx6UwAABrEjcAQGyFEJwrhQAA2CRxAwDE9kgIzqlvAwBcInEDAMR2IATnSiEAADZJ3AAA0ezsH+2t/uyKxFfz5XQ8EwYAYJPEDQAQUyEE50ohAAC+JXEDAMSkvs0F9W0AgO9I3AAAMRVCcK4UAgDgWxI3AEAUO/tHRVDfZm22nI7nwgAAfEviBgCIpRCCc6UQAABXkbgBAGJR3+aC+jYAwJUkbgCAWAohOLOcjk9FAQC4isQNANC5nf2jA1E4VwoBAHAdiRsAIAbLpC5YJgUAXEviBgCIoRCCc5ZJAQDXkrgBADq1s39UbQG+JxJfLZbT8UwYAIDrSNwAAF0rhOBcKQQAwE0kbgCArj0RgnPq2wAAN5K4AQC6VgjBOfVtAIAbSdwAAJ3Z2T8arf6MROKr+XI6ngsDAHATiRsAoEuFEJwrhQAA+BGJGwCgS4+E4Jz6NgDAD0ncAABdOhCCc+rbAAA/JHEDAHRiZ/9ob/VnVyS+mi2n44UwAAA/InEDAHSlEIJzpRAAANuQuAEAuqK+zYUPQgAAbEPiBgDoSiEEZ5bTcSkKAMA2JG4AgNbt7B8VQX2btVIIAIBtSdwAAF0ohOCcZVIAwNYkbgCALqhvc6EUAgBgWxI3AEAXCiH4arGcjmfCAABsS+IGAGjVzv7RgSicK4UAALgNiRsAoG2WSV1Q3wYAuBWJGwCgbYUQnCuFAAC4DYkbAKA1O/tH1RbgeyLx1Xw5Hc+FAQC4DYkbAKBNhRCcK4UAALgtiRsAoE3q21xQ3wYAuDWJGwCgTXaUulAKAQBwWxI3AEArdvaPRqs/I5H4aracjhfCAADclsQNANCWQgjOlUIAANyFxA0A0Bb1bS6obwMA3InEDQDQlkIIziyn41IUAIC7kLgBABq3s3+0F9S3WTsVAgDgriRuACBfewl/t0LznPvkmAMA7upnIQCA7IxWr3f1Pz9O9Duqb3OhvO8b7OwfFeEsaVLFdbGcjp9H+i2v67/V5881LQC0T+IGAPLyYvV6tXrthrR3Kio01VdVkmV2m/9gZ/9ot47fOlHzbSx/S6Bt/1y9TlavN5oYANolcQMAeRiFs1k2RepftK5vs6vJvjrdMl6bSZrRDf/65LaJoJZU7VvNvnkSzL4BgFZJ3ABA+o7D2SybXBxosnPf1beplz1Vr1/rv9smuRbhbJZLSqrv/1f9vY41NwA0T+IGANJVzcJ4F/IrCKu+zYX5zv7RQbiYTXOftny7nI7nif7OKrG4nn0z0+wA0ByJGwBITzUDY13LJkeFJjz3saH3qWbbpF5PpkpKbda+WWh+ALg/24EDQFqKevCbZdKmXgZE814up+NcEiGv6mPYsQAADZC4AYA0rIu9VjM0Rhn/jieasnHz5XQ8yew7j+pj+XVQqBoA7kXiBgDiq2qgVDMUXvTgtxSas3HPM/7uL+pjW8FqALgjiRsAiKeaifC+fo1y/zE7+0fV79nTrI0ql9NxmflvGG0c52bfAMAtSdwAQBzVDIS/Qr9mIhSatXEnjnkAGDaJGwDo1iic1f7o4+wD24A3a9KD2TbfWs8yy72WEwB0RuIGALqzrvdR9PT3mUnRrJMe/7Yi9KeuEwC0SuIGANo3Cj3fYWdn/2gUzKBo0slyOp73/Df2ZSc1AGiVxA0AtOs49HuWzVqhqRuzWL3eDOj3FvU5cqzpAeB7EjcA0I69ejD6KgxjJx31bZpTzbZZDOw379bnyp/BzmQAcInEDQA073iAA9BCszdivpyO3wz4968TnscOBQA4I3EDAM0pwtl2x6+G9KN39o+qwfZI8zfipRB89ao+lwqhAGDoJG4A4P6GXmTV4LoZ5XI6PhWGc6PQ86LeALANiRsAuJ8i2NZYfZtmnAjBlV6EYRT4BoArSdwAwN1UMwDeB1sZBwPqRkyW03EpDNca1efa+2D2DQADI3EDALd3EM7qbxwMPRB1fRsD6fsz28a5BwBXkrgBgO2NwtkTf0/9Lw+kuZ9q+++5MGxtd+M8HAkHAH0ncQMA21nX2ZCouEx9m/tZrF5vhOFODoL6UgAMgMQNANxsFOxsc5NCCO6lmm2zEIY7G/qObgAMgMQNAFzvONjN5lo7+0ficj/z5XRstk0zivpcPRYKAPpG4gYAvrdXDwJfBbNsbvJECO5FQeJm7dbn7J/1OQwAvSBxAwCXHRv4ba0Qgjsrl9PxRBhasU68HgsFAH0gcQMAZ4pwts3wK6H4sZ39o90guXUfZtu0bz37phAKAHImcQPA0CluejcGw3d3upyOS2HoxF5QXByAzEncADBkRch3O+HT1et5xM9vexvwWTjbJrv6jb9F/q1Ne5nxd39eH3u5eRHMvgEgUz8LAQADtJ5lc5jhd5/XA//Yg+eDhn9Tlaj5VP29ajbKzv7RQU+OvTer3zfP+PtX3/1p3f7VOTTK6LtX37WafTOpzyHbsAOQBYkbAIamGnC+C3kum6hmoJzEHnDu7B+N7jFgr777OklThrNEzTa/59ceHHuL0J/aNqd1+1V1ZHKbsXZY9wO5zh4CYGAkbgAYiipR8y40O1OkK1Wi42U9UE5BcYt/t6y//+dwtpPS/B7tl7u3WyapcrGoj8sP4Wz2zV5m/cH7cLHk0OwbAJIlcQPAEFQzAl5lOPivBpNvQ3rbGl9X32YWLidpZg1+ZpH5MThfxeO4p+dXGc7qEFW/7/fMzrOD+tiqZkK90VUCkCKJGwD6bBTOZtnkOOivBsPVTIB5gt+tCBd1aT6H2y15urV66/HcDWH77+NwVj8mt3NuXfPqScLnHAADJnEDQF/lPMsm9dobjzsusLuX+bFYzT6aDOS8q46LxyHPWlJFONt5yuwbAJJiO3AA+mavHny9DvklbarB4i8h8YKpEXZFGmV+TJ4M8Dw8rY/l3BIg69k3f4b8E4YA9ITEDQB9cpzpgKtaclTNUrBF8dVGGX/306u2Nx+IdfHix/UxnpN1AvjY6QdAbBI3APRBUQ+yXmU4sK1mY1SFXUvNeK2ctwJ/qfnOixdH38r+Dl7VfUuhGQGIReIGgJytlzV8DPnNslkPZo8141btnKNJhGVlKTsOeSYp9+o+5nXox7b0AGRG4gaAXBXh7En4i8y+dzXj4Gk4Wz5iUL99W4cM29lsm+/N62P/achv9s2LYPYNABFI3ACQm+qJd7VbTfUEfJTZd8+i+HBKMt4K/G1b26P3RK7Fi0d135PbjlkAZEziBoCcVFsM/7V6HWb2vRUfvrscd/aZB9tJbyPn4sWHdV90oBkBaJvEDQA5qJ5sv69fOT3lVnz4/nJM3JyYbXMrZcizeHGu/RIAmZG4ASB1hyHPJ9vrweixJrz34Dgns+V0PNFsd3Ic8kxy5joTEIBMSNwAkKpRyLOWhOLDzXqU2fdVkPh+5iHP4sU5194CIHESNwCkKNfdWyZB8eE2BsS5KJfTcanJGrEuXjzJ7HsXIc/d7gBImMQNACmp6plUT6xfZzZgn4ezWQLPg+LDbRwTuXiuuRq1qGOa2+y13boP+xjyrNEEQGIkbgBIxXHIc5ZNVVC1mhlQasJm7ewfjTL6upPldDzXaq0o63PsJLPvXdR92rEmBOA+JG4AiG2vHty8ynQwaVDWnlEm33O9rTXtOg55Jklf1X2c2TcA3InEDQCxrJcT5DagyXX5Ro5yOS7e2v67M/OQ57LEdYI6t2WgACRA4gaAGIqQZwHPScizYGquchjgzlevN5rKubilXAuvAxCRxA0AXQ/E10U7Rxl972pwrvhw93LYCvzEbJtocp39Ngp5FmEHIBKJGwC6crB6/RXym2Wj+HA8qQ9qZ8vpeKKZoitDnsWLX9R94oEmBOAmEjcAdDH4fl+/cnq6vB4MHmvCaFKvcaMgcVqOQ35J1lz7RwA6JHEDQNuqAUlOT5QVH05ABluBl8vpuNRSyZmHPJc1HtR9JQB8R+IGAC5MguLDqRgl/v3MtnEuA0AnJG4AQPHhFKW8TGqynI5nmih5Zs8B0AsSNwAMneLDaUq13sci5FcEd+jKkGfxYgD4SuIGgKEP5o6FIkmpbgX+djkdzzVPlo6DJC0AGZK4AWBoqhkTVX0SyyfStpvosfNG02RtXp/7L4NlkQBkQuIGgCE5DWdP3A2+05dijZuXy+nYYL8f3tR9walQAJA6iRsAhmAezp6yPw2esicv0a3A58vpeKJ1emVR9wlm3wGQNIkbAPquKkj6W1DXIiejBL/Tc83SW2XdRyheDECSJG4A6Ptg7DiYZZOb1JZJlcvpuNQsvbao+wpJXgCSI3EDQB8HYOviwzPhyFJqhYlfapLBmAXFiwFIzM9CAEDP/GLAlb2UtgKfLKdjCcDhqYoXT1av/wgFALGZcQNA37wKaW4lzfZGiXyPKgGo7skw7dZ9CQBEJ3EDQN+8WL3+Wr0OhCJbo0S+x9vldDzXHINzUPchL4QCgBRI3ADQR9XT8ver18eQ5g5FXGNn/yiVwsTVbJs3WmRQRnWf8T6YtQdAQiRuAOizYvX6M5ztFkMeUhkwnyynY7WShuO47isKoQAgNRI3AAwhEfDKoCwbKbTRfDkdm20znOPtz6A2FgAJk7gBYCiqJTjVMojXBmhJ+18JfAfbf/ffbt0XfKz7BgBIlsQNAEOjeHHaYg+iy+V0fKoZek3xYQCyInEDwBApXpyu2O1h++9+H1uKDwOQHYkbAIasCIoXpzi4jmWynI5LTdBLx0GdKwAyJXEDwNApXpyIBLYCN9umf4qg+DAAmZO4AYAzihfHFzPu1fbfc03Qq2NJ8WEAekHiBoC2/bF6LTL6vooXx1NE+tzq+LT9d3/kWHx4UfeVAPAdiRsA2jZZvX5bvcqMvrPixXHE2gq8mm2zEP7sjUKexYfLuo+caEIAriJxA0AX5qvX49XrZchr9k0Rzupj2Da4GzGWtMyX07HZNvl7EfKrU7Wo+8THdR8JAFeSuAGgS9UA+ZfV6zSj77yulVENCtXKaNcowme+FPas7dXnZm61qU7rvlDSEIAfkrgBoGvVU+an9Sun2Te5DhBzMur488rldHwq7FnKNaGaa/8HQEQSNwDEsn7iPMnse6+XZChe3KBIW4Hb/jtPByHPJYyTkN+MQwASIHEDQEzVE+fnIb8aD6NwVgD1fVC8uCldz2KaLKfjUtizkut5N6/7uOfBLBsA7kDiBoAUVAPoaleV3Oo95PrkP0VFx59ntk1ecp3p9ibkt6seAImRuAEgFZs7rMwy+t6KFzejy63A3yyn47mQZyHX2lKzkOdOegAkSOIGgNSU4ewJdW4zIhQvvn/8urAIZtvkIOeE6EkwywaABkncAJCq43rwM8vseytefDejjj7n7XI6NgMibbkuQZzVfdaxJgSgSRI3AOQwEMptucEoKF58l5i1bb6cjg2qnTdNWy/zzDHRDEAGJG4AyEGuBT4VL95Ch1uBWyKVrlxnqpUhz8LqAGRE4gaAXMxDnsU+FS/eLkatD7CX0/FEqJOTa22ozWLqc80IQJskbgDIzXr2zakBam8UHXyG2TZpyTmhWfU9vwSzbADoiMQNADmar15P61duhWbXS0IKzXju320PtJfTcSnMyShCnksIFxn3OwBkTOIGgJytn3znNvtmtHp9DGdFWM2+ab8Q7UshTsJufcx/DPkV7c61rwGgByRuAMjd+il4jrUmqkKsfwXFi9tcKvNmOR3PnSbRvaiP9dyKD8/rvsUsGwCikbgBoC/KkOfuLutaH9UshKEWL25r1lE10FbbJq69+tjOsbZTrrvZAdAzEjcA9EnOO70U4azux3EY0PKpnf2josW3f7ucjs2SiGO3PpZzrOc0D3nuYAdAT0ncANBHZTirR5HjbItXYVjFi9tKUs2X0/GxUyGKoj6GX2X43U/qvqPUjACkQuIGgD6rBu7VUodZZt97FIZTvLit5WGWSHUv5+LDs7qvONaMAKRG4gaAvlsPyKqBfG7LHoZQvLiNrcBny+l44tDvVK7Fh9d1kHJM8AIwEBI3AAzFcciz0GjfixePWnhP2393J+fiw2UwywaADEjcADAk85Bv0dEi9LN4cdPJqHI5HZcO9dblXHw45yLmAAyQxA0AQ7Te5vc0w+/et+LFTSehnju8W1eEfIsPn9bn/hvNCEAuJG4AGKr56vW0fuU2+2YULpanZKuFrcAny+l47tBu1XrZ3iiz773YON8dIwBkReIGgKGrnsD/EvKcfZN7zZsmZ9usl7/gmOvTOQ4AEjcAEC6exqt5kW8S4O1yOl4IKRvm9Tmd46w6ADgncQMAF8qg/kWXmtoKfK7N+Ma6jlUpFADkTuIGAC6z40x3Rg29z4nZNtTmId+d4wDgShI3AHC1Mpw9sT8RitY0sVRqtpyOJ0JJfa6aZQNA70jcAMD1qif2x/VgcCYcjWuiOLGCxMzqc/Q4mGUDQA9J3ADA9gNDs28a0tBW4OVyOi5Fc9DWs2wkVgHoLYkbANjecTjbVrgUintrYrbNc2EcrLI+F4+FAoC+k7gBgNuZB8VPm3Df+jaT5XQ8F8bBUTwcgMGRuAGAu7Hd8P3cZyvw9eCdYSnrc87W7wAMisQNANzdPJw9+X8azL65rdE9/tu3tv8elEV9jpllA8AgSdwAwP2dhrN6G6dCsbW7LpWqBvFmXDi3AGAwJG4AoBnrWQHVay4c19vZP6oKE9+1OPFLs20GYb5xPmlvAAZN4gYAmlXNDFCH42Z3nW0zX07HE+HrvXX9KLNsACBI3ABAG+x8c7PRHf8723/32zzYsQ0AviNxAwDtKcPZzIETobhkdJdYLqfjUuh66yTYpQ0AriRxAwDtqmYOHNeD0plwfPXrHf4b23/306w+N46DWTYAcCWJGwDodoBq9s3tCxNPltOxpFf/rGfZaFsAuIHEDQB06zhYElLc4t9dBMmuvinDxSwbAOAHJG4AoHvVDINBFmGttwK/jbfL6XjukOmFzaLdZtkAwJYkbgAgnvW2x+WAfvNttgJfBNuq90VZH+vaEwBuSeIGAOKah7MZCNVW10OYfTO6xb/7cjkdK1ibt0V9bD+uj3UA4JYkbgAgDZPV65fV67Tnv3O05b83X07HE4dF1k7rY1o7AsA9SNwAQDqq2QlP61dfZ5psuxX4c4eD4xgAkLgBgBStZyr0sR7INsWJy+V0XDoMsvQmDGPmGAB0RuIGANK0uQPPvEe/q9ji33mp+bMzDwPdKQ0A2iZxAwBpK0NPduPZcivwyXI6tlV0Xoa4OxoAdEbiBgDSt559Uw2Oc05qbLMV+InmzsasPibNsgGAFkncAEB+A+VckxujH/z/T5bT8VwzZ+Ek5J9IBIAsSNwAQH6O60Hzp8y+9+iG/181Y+ONpk3ep/rYOxYKAOjGz0IAAFmahfxmO9y0FXg128Zym/QdCwEAdMuMGwCgK9cVJ54vp2OzbQAAriBxAwB0pbjm/277bwCAa0jcAACtu2Er8HI5HZ+KEADA1SRuAIAuXLcVuO2/AQBuIHEDAHRhdMX/bbKcjkuhAQC4nsQNANCF0RX/N7NtAAB+QOIGAOjCt1uBV9t/z4UFAOBmEjcAQBdGG/+8WL1s/w0AsAWJGwCgC5vFiavZNgshAQD4MYkbAKBVO/tHo43/OV9Ox2bbAABsSeIGAGjbaOOfFSQGALgFiRsAoG3rZVLlcjqeCAcAwPYkbgCAtu3Wf822AQC4JYkbAKBtj1av0+V0XAoFAMDt/CwEAEDLqhk3z4UBAOD2zLgBANpW1baZCwMAwO1J3AAAbVPbBgDgjn4SAoB2PXj48J+G3/Lx31++lCILQA+uaedW1zZjE4Cr+l4hAAAAAEiTxA0AAABAoiRuAAAAABIlcQMAAACQKIkbAAAAgERJ3AAAAAAkSuIGAAAAIFESNwAAAACJkrgBAAAASJTEDQAAAECiJG4AAAAAEiVxAwAAAJAoiRsAAACAREncAAAAACRK4gYAAAAgURI3AAAAAImSuAEAAABIlMQNAAAAQKIkbgAAAAASJXEDAAAAkCiJGwAAAIBESdwAAAAAJEriBgAAACBREjcAAAAAifpJCADa9eDhw39EAQBu9veXL8YmAFeNJ4QAAAAAIE0SNwAAAACJkrgBAAAASJTEDQAAAECiJG4AAAAAEiVxAwAAAJAoiRsAAACAREncAAAAACRK4gYAAAAgURI3AAAAAImSuAEAAABIlMQNAAAAQKIkbgAAAAASJXEDAAAAkCiJGwAAAIBESdwAAAAAJEriBgAAACBREjcAAAAAiZK4AQAAAEiUxA0AAABAon4WAoDWPRYCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACALPwkBABnHjx8eCwKcMnk7y9f5sKQVT82Wv05FAm4sOrHXN+BrEncAFwMeP4RBbjk6WrAcyoMWfVjB6s/70UCLqz6MWMeIO/ruxAAANd4JATaDACIS+IGALjOgRBoMwAgLokbAOA6owcPHx4KQyY3dWdtNRIJAOgX6z0BLgY9atzA9xar1y9/f/myEIqk+6/d1Z+/Vq9d0YDL1LgBsr/OCwEAcIMqEfCxTgyQ4s3cWdt8DJI2ANDPa70QAAA/sLd6/fng4cNCKBK7kTtrkz/rNgIAesi0QYCLAZClUvBjs9Xrw+pVCkVUxer1JEjYwA9ZKgXkTicGUJO4AYD+kbgBsh+nCAEAAABAmiRuAAAAABIlcQMAAACQKIkbAAAAgERJ3AAAAAAkSuIGAAAAIFESNwAAAACJkrgBAAAASJTEDQAAAECiJG4AAAAAEiVxAwAAAJAoiRsAAACAREncAAAAACRK4gYAAAAgURI3AAAAAImSuAEAAABIlMQNAAAAQKIkbgAAAAASJXEDAAAAkCiJGwAAAIBESdwAAAAAJEriBuDCXAgAwLUdICUSNwAXZkIAAK7tACmRuAG48EEIAMC1HSAlPwkBwJkHDx/urv78RyQAoDf+9feXLwthALIepwgBwJn6xm4iEgDQCxNJG6APzLgB2PDg4cPR6s+fq9euaABAtqqEzW9/f/kyFwogdw+FAODCP//8s/jpwYPl6h//T9EAgGz977+/fPl/hAHoAzNuAK7w4OHD96s/ByIBANk5/fvLl6fCAPRmbCIEAFd6vnqVwgAAWSnrazhAb1gqBXCFf/755/9bvf746cGDqtbN/yEiAJC8N39/+fJ/VddwoQD6ROIG4Aarm7//96cHDz6t/nFUvwCAtJSr1/O/v3z5v4UC6CM1bgC2VO84VdW9+TVI4gBATPPV63M4q2czFw4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAr37q2e8p6tej1Wt39dq75t+brV6L1etT/c9l/b8BAAAAaNBo9Xq3ev1n9frnHq/34SzpAwAAAJCEnGfcjFavV6vXYcPvW65eJ/VfgCE7rPvaLs1Xr4nQw8129o+KEOeB02Q5Hc97GM9RC/eUg40n6GvvbLbqE05F/s6OY/Tj9f1rq37OtEEOwtksm90W3nt9cr4JZwkcS6iAoXoWYWBYBokb2Pb8POz6Q1cDiuOexrO6t3wV4XPLLm74gWz62mr8KXFzN6NI/fibLj7kQYYNUp041bKm3ZY/58Xq9bGDzwEAuK0iwmeWPY7noxgfupyOS4cyJG1PP6utbjAPHU30yC1xcxjOZtp02fiSNwBAMnb2j6r7klGEj5654TdAA8mA9kjm3kuMBHxn7ZVT4qYI3SZtNk9WyRsAYJADiQ2f+xhMiTDgmr6h0Ce4NqZyXcwlcVNdUN9HPgjeORcAgAQUkT63r4MKiTAghb5B4ia/a2NnbZZL4qYqMhR7xstB/QIAiCnGdPDFcjru66CiiPS5pUMZ9LUbPgn5ncVKwHfWj+eQuBmFs0LBKXjtnAAABniD2ucnwbESYXOHMuhrB9LPtq2I8Jlllx+WQ+ImpVkuoxBh600AgMrO/lF1LxJjFnKfnwRLhAHf9rWd177q8azGLvza9348h8TNs8S+zxPnBQAQSazp4L0cUEiEAdcoOv68UsizuzZ2Wqcs9cTNbsQblFROYgCAtUeRPldhYvEEiYD2SObeXaycgRk3CVxMUzwwAABi3IPMe1yPJVYirHQog74hVhLAdfHeFkHiJgu7QgAARFBE+Mw+DyhiJcIWDmXQNwykn3VdbMADjQAAkL6d/aNYM34/9zisg7jhB27V145Ctw/q7TJ3PzEKE3e+tC31xI2nEQAAZ2IlbsqeDs4kwoCrFPpY18YfMOMmdkAAABKlMHH+N/sGaZC+rmdwSObe3Sh0vG17rH5cjZu7mQsBANCxKE8Ve1yPJUoibBXP0qEM+tqYSQBtde9cQOfXxdQTNykexIsgcQMADOMGVWFi8YShKfQL+vHU2iuHGTdlYt/n1PkBAHRpZ/+oiPTRfZ7CL3EDfNvXdr6blF3m7iXGzMlPMX5oDombP3wfAGDgikif28tEQ8RE2CeHMuhr+97H9vzaaMbNNaoZLqlkIctgDSIA0L0Y2532uR5LrMLEBmmgr92kMHF+/XiU62IOiZsqafM2ke9y4vwAAAZyg1r2OJ6xChNL3IC+dij9bB+vi9H68Fx2lToO8Z9QnDixAICu7ewf7YY4250qTGyABkPrazvtGyRz7yVGAj5aP57TduBPQ7wlU5NwljwCAOhaEelzezmFXyIMuIbZNtor2etiTomb+er1OHSfvJmsXs+dFwDAgG5OKzPxbJTCxJC2Qh+rL0+1zR5k1jhVoB53GLCXQdIGAIgrxnTwRY+n8BeRPtcgDdLWdWFiyVz9+NYeZNhI6+TNmxY/o1y9fmv5MwAAtjGop4odiJUImzuUQV87kH62j9fFMuYPfpBpQ1XLparZMFVyZdJwYzwO3c7qAQC40s7+0Wj1ZzfCR/f5SbBEGHBVXzvqcjwrmXsvMRLwUa+LDzJvsOoiWC1l+iWcJXJOw+1r4JT1f1u9x+OgSBQAkI4i4j1WXwdnEmHAtxQm1l5JXxd/7knDzcPZsqb10qZR/bpqS7cq4Iv6v5k75gGAhP0a6XP7OqjYE08ggb7hs5Df2SB3Bvy5p405DxdJmVPHNgBgMLH9fdRyOl70NJ6PIn2upVKgb9hUCvmdFTGuiyHypI8H2h0AwA3qhj4nGSTCgBT6BsncvPrx6O0lcQMAkKCd/aNYy3r6PIW/iPCZpaMZku9ru6x9JZl7PzFmTka/LkrcAACkqYj0uWWPB2cxqGUBaVOYWHsl32YSNwAAaYpSmHg5Hfd1UBErcWNJBOhrN0nm3q8fj7EzYPTrosQNAEC6N6hd63OSIUph4h4nwqAvCv2s62Lq7SVxAwCQmJ39o90gceOGH+hd3yCZey8xZqJK3AAAEH8gseGzmDbKAA0StrN/VOgT9OM5XBclbgAA0lNE+txeDioiDM6SuuEHkkkEmIWX37UxieuixA0AQHpiFSbu66CiiPS5Bmmgr90kmasfvxOJGwCA9FjWk/fg7KseJ8JAMkA/67rYIYkbAICE7OwfjVZ/RhE+WmFiAzQYUl+723Ffu1hOx3ORv7PBFiau/Kz9Ifkbzd36n4s7dDSL+p/n9YsLmzu23Gb3ls1YbsYY9FO366cW39wQOZ8uxzSGXk7hjzA4W/vkUL7UDqONdhjdsk0u3dMY/HZ23uzdsm/fbKfZqp1S79PVt8lLEeEzk+nHJW4MVjc7rP91hw5ssXGjt9josHVMt79wVJ3Rv+t/3hwINa3caLdZnYToc3uNNmL668b/bvpCvKg799lGXEmnz9vbOL+2ufhv9mPV3//W586QkwujOm6/1nG87cBrW/ON1/8MpJ+KPZjYvD642TdIu89gf7TRV/x745q72/DnfHvMftr43xI7t4/n3kb/PmrqnKnbad2Hf15fRxNK6HTdN0jm3u9+bhThc824ofVOaH3h/PfGP7d1sB/ccKDPNwazpaa5NACq4vbohvi1fZE6+GaQWtZtVWZ+s7m7Eduio07+qmTAOqYf1jeSDvvObLb/3j2Oo+Kbdn21kVjYbNu+JnLWMXjS4bkUfnC9WvdPn3t+Xj2K8Jl9nsIfKxHW+8TNxoB/3efudvwVruynNxIG1et/EkwYxG639b3Skw7abf3w5GCjfdbX0NPI/U7XS2+MhfLqxxcp3Wf8lGFCoojwuccJD/7XneGj0G5ypimn6446DO+pddU2h6vXswzaaV630R+Z3HiO6huCZxFv0Le5gf+jjmsug6OPIU7Rvsd3vKD/Xh8HXQ8c1v3apCd9VVGfS4cZfNd56GESbTWo+U+E47hcDaAehx5axTNGX1bN+vjFgD/JPmMz+TuYZM5G2z0L8WahXXd/9DacJXEWHcek6772XxF+YxGxvasHAm8aHI+/inB/9zSVEyW3xE2MBkspTusT71FodylNlyfDeiDbZwf1gLLI9PvPQ7pJnPUNyIFjvxU5JG4O6/MrhYTdor75fJNpAuGwvsaOMu5vq+Nn/XBgnungqjqW/4zw0SerG+zjng5YYyTCqkHo0x7FsOofnmR4vd02cVD1HV9nHfctkVMP3HNJxk+q+6NVG5QdxKW61v3V5f1018nc+jf+GXHM+HT1m5u6141xT3oSEprAYalU2opwefppHxMaB/XN9Unoz9PqPg2CQv39X9Sv9VORidg69h0D39mtv9PvIa8ETl/6qs3r5uuQ5yy3imU9zQ9cYgxaPvckdr/XfcRu6K/17PUX9e8+T+Q0OOiM0X5Vu6U2u2ab69Hh6rt/vT9axX/Scrt3qYwQz3cRz903DZ8/g98Z0HbgadmtO6zqJKueDn2sb6aLnv/uUf2b/wp5PA3YZuDwV/2bRj1rq72N4/M4wsXgsGex7dux39X59Wfix8A6gVO160Hix9/HnvZV6/7qdd0O70M+MwV+jfS5ZY/7DPG83YC/WL3e1+fOi9DvpM11fceLum/Msf2qxMf6XinXMcTX+6NqttzqdVwv82qjnbv0uePj4EXE9q+WIL5s+HiI0Q8l9UBD4iaNG/zD+qbyP3UnezjAi+TmIPZjSLdOyTaDoI89HQRdNzA97ujGu6/JsM1j/8/Q/0TtfY6515n1D7t13/4+wT79xcCOt4O6HXIYiMZok3mP63zESoRlN4OpTtis72MOArNM269P90rr+802jsdHfT2e6iW3ryO1WXUtaXqZaJTrYkhs1rTETdwbs3cbg1EXyMux+VjfXOdiaIOgzQvqo5bf/30YRjIs1AmJj/XFdldX8F1cXmT6/Q/qvr5I5Jx9N+BjbBQuZuEcJxqDGInJPu9+FCWeOSXCqiVRq9f6wVkRWPuUUfu973H7zVtaMtVprLqo27Mh5myx5y3sFBYjAV+mdiKocdP9DfN6K7yRcPwwVq/rE/V54t9z6Im3Dy29b3VBTXGmQhde1MfU82DryIMQd412k33Fx7pNJ5G/w15g/RS3usYkU0C2LiIaw+cet3WMmGaRCKuXn7wIcTb+yMEsgzZct1+f75VOWojbXl+PpdVvex3xOv+mpbpQMX5PctdFiZtuHYZ409Zyjll1sla7zKT29Gpd72Xog6A2EguvQ76zK5oyqgfZSVW0j3D+v+vZb1pPYe+6TSVtrjZP8LrSl348hUFtrHh+ziA2Rejv8uPenxd14eica9hsa9HSbJteFiauz+tY989N17XZFOM4Ty5xa6lUt06F4M6d68eQ1tOEPYOg80FPkx3benD5wmF/rnqSNsSZR4ehf0mbzTbt8rdJ2lzvj8S+T5R6LB1P4e9SrEFtsjM1qlk29RP5oSxBvvP9TarL3erdooayPP9tS+/bdX2bz12c2/X9YgzVudLWCgkPNGoSN3kPcockZpGtbx2E9BJJsTTZqY2C9fWOubPfmO1uHrdwGLpLUMacNp2yRYLX5Bj9X5/vSyTCLg/sinrA7+FIhudFnXR7F/qxfHjbPvpNT5IBXRxPMY+Ll6t+r63fGOO6mGQfLnHTvQ9CcK+BznECA+ih1l1p83jeq28mDS5vjtEQkjcpJWnb9jq0vw38i2Cr+eskNQu2flo6MkDNenCW7A1/taVyMMvmNj4l1n6juv2G1J+/bXHWU5d9w6LFpMb6+DgM8eptTlpazrYWIwGf5HVR4mbgN4oZqpYYFBFvAN9pgsaP56EkJIJYcYU262QNKQl2Fx8SPL9j6HNh4sHv0FXP0vgYFCDOth3rWk1DfLg1aSmeRZ+OpTqp9zriefKy5c9QmLgmcRPnAJ8Lw70HOl0PXA2Yv9dE0mYkro5FWpvFJ2nTfh/WpCLS55Z9bFw7dF0a8BdO99tJZblbPZNiiNf8SQtbSsdKBLQ9eyvWEqmvdW1argW1G8ycPCdx42YxR9Vgv8v12bthOOuJu7wQ7QbLzu5z0/FRGHrVpzU9m+/QYC2763Cseix9XSoV6/hPIp514srSqLzb8HDA958nLb73o74cT/USyFh93UkH148YSZsqETVP8aSQuInjDyG4t1cd3ozY8rudgc97cb33xczSvf44CM2uT7cs4mYp1puLcfNd9riNYyTCFikkwgY8S6M358VG0maI2pxtEyMZULZ0jOxFvNafrtroTQefE+O6mOzDDImbOCyXymdg8iLEK/aVsvk9j+HXwWyAJhwGu4P0yeuGBlrVcTESzptvOlP6MnWNghiDbIWJexbPgQ/4m/JZG0b1tsXYdl0EvpVt5SNv/V3d/z/v6LNiJOA/pXpiSNzEUwpB8oOT6r09tW5+0HMg2dD4YN/MpX4YNXRu/C6UPxxcLxL7TgoT5z04S+KG34C/0T5CG0YaH7U8a60v24B3ufLgW09brmuzqRjS+f8jEjfx2Ba8GYctvre6Ns0fvyM3la0dq/TD7/e8GdsLEnk/kuJy5UeRPrfsaRsXkT7XgD9/0Za7acOvTnrWN3xq4TiJ+QD0ZYfnxyjSOCzZ66LETTzVjIWFMNzbs5be9zBYynPtTc09OjXJsHZUA/VjYeiF6vy4z0y/Z0K41fU3xXM4xgB13uM+MYYoN/wG/I2KlbSpjtmh7wRYdrCbV9aFievZhLHO9a7q2sTsx+cpj89/1j9Hv3k8FIZ7GYWzpTdN3ojvuni2cmNatVMhfK15VZ8HM6HIXnVdeHnHmwc1uX58UzZP8HvF6BvnEbfMbtuTGPHscPmAAX97PkVow+peVjHpbmZDdpoMaCERFWs31uq6+bzjzxxknbKbSNzE9SFI3DThUWg2cfPCxfOHx+1txXxCMCTVzftjYeiFqh86vuV/MwqKEv9IcrNt6oF3DHv1YJFMb/gzGvCXNxyDu0Nux40is0O/76wSn5MOzpfdXI+l1fev7guKSO3zPEJiOsYS4k8pnyQSN/FvIBc663urnjC/bOi9qk5dQeLmBz6SYd0oQvMz0IijqnVzfIf2T20AVA3Y/htunqk3ChcJp0d1X9FWMiPF+jZqEvVDp4WeEx7wz+trUDUAKrcZ7NXJy1F9LjyK3JeVHX/eO33AVycdfEbXx9WswfM95tbfJx0sYUvlnsaMG354gTiI/Pnb3FSmPOhe3/TPG3gvSZsfd2iLO7RPDnGd16/rsu1tDyib8jpI3PTBbrh9Eu5RAt+76h+qrVwnDfTJ60LLv9Y3cHsNfLcUb8oeOdx7cz/XdV+f0vWoOuff3qVwaf3fzNb9XZ2Uqvq/Zx0P3jpd7lbPoEh9ees6Af/5hj59fR9+13ul1mfb1LreWrrJ2RuxakRWydfjCJ87qDpl25K4ie9DS532ehBadbj/3Rhw3+fGtag75kf1d04pmbPXwCBhN+RZH2L+g9/eZOLtLsukUk7aTOrfVIbbJaSqc6GqoXAY0ktqjurvNQnDsti4uSxv6OvWN5jrNkw5Efcs3C5xs5fA+XTX2jzXDRhm3/TR63Yrwu2XhaWa0PS0vQe6fCJdD/gPE7qOnjRZ6LpOnkxWv3Meuk3czDpsw5RrE1VxqBLwp/dJZNW/sdgYN1znbU/72llDx8pxpOtE1fZPB3RdTL5GpMRNfNWN5H1rf5T1wbbOhrd181BuXKSf1zcNXT8NuU4TdW5yWM6zbt9PVwxqfmT9BGT9BPsu2wbfNsajkF4dp/WMgDf3GGCW9etl/ftehbRqi7wKw0ncVO3wxy1+73zjPDreOEZ/T/D8XyfItz1OYyYA1teFts/d041+aK+O0bYJuA+JHsMSN/kb4oC/6keft5yw6vrc+NRRG66XuaV4PW1sWczGTKo3N8yiWnR4v9LpeKWJbbPrAvKxHoA+jVFwfWNcF+P4T5rETRqDyNOw/UyP+wzc27hRn9SDnteRBz1NXNxT3kZ3UicbZvc81spvOqb1hXSbWVR3ma31e2JxrJI1J6HZrf7W58FxSGd20ai+QUn+InTfG8wGfuO8brvq2HgX0pt1d7DlTe0o4nesrmHPI3zu+hp4HC52GHx2w/UgxcLERaAPurwXS6HQf9UnvexgUPdrT9sxtYc9VTtWSbjW+sj1LKpwNpNqr74/rMYPb7tIDkQoAl828J1jbuwRq65Nk+O62/ocEvfAtTYJP3oKWHWk1ZP9X+rX87rzS2VKV/VdHoe4+97f9wQ/CGnuxjLZaPM22nt9Ia3e/1/hbErkaUODnt2QzmybRX2MvmzxOK0Gj7+FdLYa/j3018u6PcuGj5Gn9bmwSOi3brut8Shye8RWnXdv6nPwl/o7ze7Rf/X55pRMb/gjLpm4dL6vBnRd7TBTdPnDuhio1snaFwkdu1Xf+EubSZsr4jyrjqH6Ov6mo48tOo5rE7O33kW6tseqaxP72mipFFt3mu+u+L99CBc7T6VuVnfAsbal3A23W1LwrWcJxrOtZM2PjsXTOpYv6risLxq3XWaQSh2kLmM5qweOHxO4uV4nI+c96ivXyZU2b64ndTumssVu6nW3ThM8xub1YOBNfQ78HtLd4lNh4n7oYsAfc1eZdf/7sqMisuvZBl0OWru633qX0HFbteebWB/e8YyOrGZvrY7/g0jX/0WIM4N2UxHpdyefuDHjJp3ByKy+2aym/v9SD04mIY+kzWYn9Tbi5991oJxaUeKq3R9H7kCq4+44XJ7tc9sL7O+JHJNdx3I9uyeFwexhz/rJpmfZ/Oi4SUXR0L/Thg+JHzfVeVjNvjHjhjYHoF1cY2IO+L/2v10lbSKdG61fW+oZU6NUrqcxkzYD6Gtn9zhORhHP9+dNFhpv8Z4nmfbqksRNOp7Wg+TjkPcT8vsUfI0ltaRNaks1qu/02y2/0yiBAckiYixjVuLf9Cz0wzpp0+WFdRbSWAIU6yZmW/PAXW/Ou55RQL4D/heRr6lPO0pOxez3PrfchtW5nsIDrXXSphzYedrl+TO/Z/Ij1tbfb7pcMneDXyN85qccDmKJGze/bVwQJpkNbp4kErtJiD89sSkp3Jw8DXEz6CkM/EehH0/0X0ZqyyoRncJNTMrLaWaBXAamZHgO1Am+mEuknkca5D/qUzvWbbibwLH6OEISLqoIReDvM9vmRaRrQ1V3KJWHVTHOk9McjmWJG9rwIaPvmsoyqVi7srQldkyrAXeZQBzeJDCwzX3WTXVuTCJ+fpsFrfswwF8E7soyqX5o+0ltzF07X3a8PCra+dFmMqNOHBwm0Fc/H1rSJtI19PMdj5O9+nyPcWw8DcM1D5ZKMWBlRt81hQFR1WH0KWkzCnGn/1fxPEkoHrGfYBxkfCylUCSvOp7eJhCLItE2KgJ3pTBxP7Q54B9FHPCfxqqBUv/uLpNVbd+3vop8jK6XRw11hmTXS2/KOxzzMbf+TqGuzaauE9V/5HIgS9yQ60WwqZvgFG6cU6tpk3ui4CSxeJYhbjJzFPKto/EykbZMoXZXqrMzzBoRuyFbtDzgiTXgn4e4SfOi489rbdZUPdumiHycDjlp03lfe8elha8iXRNSqWsT89o4yeVAlrihzYt+DmJfTE9DXjOUtvEo8nGXYgccO5uf46yblNpyEeKvf/53ou30e+Aug7lRSGO7ee6nr7NtqmLEMZPVv/alHUP82TbPh5y0qc+jUcrHUp3cexGp/zoJwzbLaMwqcUNr/ieD71jdNMd+4vmyh20fM0nwNtGYTCJfGHJckpHazUTsY+tHfVWsQVZ1Q3zskndrhRD0Qpv1bWIN+E8SGOhns3XzFgPymOf6JGKNolQkfSzVS6TeR4jLuubR0OvUvc3py0rc4MZ5uIP5vsY0VacDbpfbmifYlrMQt3jd3hbfL5ZqgHnoknIrvwpBL5QtDfhHkc6pqu99k0Bcu7xmzVtc7hZztk0KO1umoOvEzW2TubG2/n458OVzKdyb35rEDVndzGTemX/rjx62e8yYVp1vyk8OYmb1q5uCUUbHUapPQMrIbZjy0pp3EW9A9ZXEHBz3acD/MvYT+Jy2bv7B76iuuUXEUJpNcSbZbeXrrb9jzFJPeSZWl9fG1McN35G4QWcexzz0r7ZN7Jimvg39PMSdFVFkdByl+gQkdrL1phuaFPqTw9Xrr2D2Td/OR67p09sYGNdLJ2IM5spEipR2ndT83NL7xpxtc2I2RZzjadu414m9GMdI6jOxunz48yG3g1nihiEbGZhmf8OVW0xjDq5zWZpRxWie6HerbnhiPp350Q1NCk+O1lua/hkkJ667YTfbph/aGhgfhkhLJxKJa/JbN29xju+GeAns6vr5xul53temuq38+wjnubo2l2Mxye1LS9wwZKOIn/2HmPZqQL2tmNl9g8W0B2tNtGFKT1ir7/oxnCVwDh02lxRC0AttFSaOsVPbJKEZGjls3fwjMfu8lwbm0e57tp1tcxzpnsxMrAtZPkCXuGGoN6Yxv98isQFWH2JaZhKjmN9T4ibtwVpfv1t13FUzcKolVNXNqho4ChP3RePX8bq+yyjGgC6FgNYzVfZybsPa75FCmMpyt6H2tZ+2OMar4zvGEqnT1bGRw0ysru4RsnyALnHDUMUcPJQ9jeko4md/zihOZcRj3qA53Rv9bTxK9Njatn+oblb/E86miB8M+BiSRO2BlmZqPIs02J8P9NzoU/KtcuLMTPd4irj1d3V+P9dml+KR5VhM4gadefc+9zSmo4ifndMMptlAj/u+mCf83aobkRymyB/UN69VEuf1AI9L52H+Zi2eG0Me7Bcdf14bsxSfRYpd2VIyMWddHk+LLRKgryPdKz+1fO6SbGelSdzQln/7fjcOrvoo5vT/nBI3MRN3o0Dfj7Wcbkiqp4/Vdqh/1q8XoeezwiJsdUwm1/HVsXEQ4fifJzbY7/o+oo3+PNZsQrNt4va15Rbn92GEULxU1+Y7b3P94hI3DHWAGPP79bUDjTXgmmcWp7nzMnux2nCbmRq53pBUv616Gtn3pVSF06cX2kjAPzHY7/b8aHpAGyn59jVpYLbNna6XnfQJdV2bdxFikEtdm67HYPNcv/zP2m+QNou/bW6V9+s3F5y7FImb1y9Twa+2CHksZcgpKZBbBxzz5urfTsHGjrkYx/s2A4JZfYzlnCA4qF/r7Tr/CP1JeCtM3J+b/zaO+84HdqkEdDW4HYV0t27e1pNI4fvDKRm9ry2vOJ5/r8/rGPcLVcLmRLv161yRuOm3vfpVdRiPwt0SMXcZvMcawN/mRqrI4DvmZiSmW1uEOE/lRoEhOAn9mNmxXkpVvebhbDbRJOSd/I7xUGPe44Hdsxj9Wk9makwSq3vR9bnRRn2bGMm3qrbKxGUv+n3+rE7WHNT9UqwH2FV//zzjGVht94NZnysSN/0aNFed1K91Z1EMMAb/zWTAzvDa/bsLfLBkImefEm+/MuQ/6+aqa1y1lKramaqaJXASMpttV9/UjyJ89B+rm/jjPp6Iq5j+Hun8atqjCL/jQ2LN2XUM+rJMahL4ti12O+5rq3v7jyH+aoOTvvb1DTnNfRwmcZO3g/pCF2saHrfX1x2lLI3TTqSl2vrzrx7+ruqG/LB+VQOWnBI4sc6/Xs70jLC0Zq0PMzWqWRqnAz8/mj4vHkWKm2VS8Y+l3RD3/qoMZ7Ns5pr+Rh9y/wGKE+enurhXBa7WBRyrKeQjYbkV8WrnohXzgpWb2QDbiW77r+oGru+7jByGs+TUu0yObYkb8fxOpJlYKe4+V3T4WfMWBrkxlknN7RgU/ViKqZo9Uu0a9bhHSZvdFmM1yT04Ejf53Ki/rm9Q39c3qwZg7Q982uo44L9CQAf913Hod12ttcP6+vgi8e8Z44n8vMdPYWPNcGj6nIoxyPyUUkPWu+5k24YRl0GeBq4yhCLwVdv/0sNdo/acK9ezVCpt1cV8XZGcfvBkBJzHXXq6ev0Z+p/sr35f9YCjKgr5PNE22nOsZh/PRQuJsBgJqKEvk2p62XoRKW6WSaXVHl2o+p+XCS51TF0vzhUzbtLtcD7WL0kbN6jQ9ACXew7eMrvJezqgtqkGgFWi6jilL1XPKIhx7n3ucVvHGJyVPfgds8R2k6o8yrwdYyTfFpZJXdnXjnp8n1PNrvlN0uZO90FlH36IGTdpqTqbaseMQ6Ho/WCqj8cut7hxjjywLTXBoFTtXc1CeTeg31xdS3+tf3cK14a9iG3fx8FZrHh+bvh3/P/s3U1yG7fWgGHkK1dlGGYF7qxA9ArUHmQsegWmVmBpnIGswR1LXoHpFZga34FaK7C0ArdXEGV4R/kIC12iZUriD4BzcPA+VSw7uTcSif9zCKAbgflTY5vIWp8JHpU8pm/X2ZYyekPCZmtmyo0dN3r4s/n+W8IpRYECNYK/u8TFC0lG5DZzd0mMmvgdq5dOR2JZ6s4FLibWPd9IfI6ryuvz2kh7vHLQNDakdhIec07dbc7MkUISN/JGYWF55jjCAABIZ+bqS94MR6fGCt5HbhqPxMRi5WLi6ndqLILRtuQ6FHj/KuuRsSHLHPJVcLdhrpg4RX838wUGiRtZfrD/6up5bF1qPUUAgHHuSTNXX/Jm+IJEcsErMc9zMXHk8kyQCMsdZPYKk3m5+8aVgbbouN9G1VibdS779c+/plTz2kxd4E3iRs40LCTZZaMnoAEAtQv1iOPcbPF67eo6sufn2s8Sc67gN/I39MGoLByx0Rjs7xVeBhLHIDum4ZVj7biCj+nnsI+Lz3pEja/F1L1AJG5kTF1dl0TCPskAcEzxQ2DhVDq/8P+jsgCgcXdfmNQyRpn8Rt5KIkzo6Tcak3m5LyaO3S8agTLrmYarXw+eLcYQa7Fk7PFwbq2vkLjJb+pI2sAeyQChxCC6EfzdXIyM5bbgd94cV9QuxgJzsMjFxAmenFN7cGYh4FfVJgSeqpXi87cCRfeN6UvPWCsZUy760BdDlxbHHtsvrFU4iZvMHcyRtEmlL+R9cjQOUgv2VMEHyne+eL1y9ey+8XPxJOPvkwjsLNelyOWjCRJhEu1C2/ifOwkX9X4bwYC5lrG6hD6loQ9dVnJMbBP+yyhzj08ncZO3Y5G0SacvqB0AKNtvBsc5/7Nfh1dfQR36+Th50BUCu4YAvfh5NEWg/DL3h1B4MXHpd/ywpmNs0PK5LwWPkWrkkzbmdhKTuMljeKJF6bpHXnyDD0kNRYBKFod9pnHe331z6GwncPy8fGa4rZi8mNhYIiz35+gUVul+4fUotf5g3f3z2NASa35P3rCz/86FxQ/1gnrNIss3exEmgT4s9vzfb8M/b7Nw9xPZibvbjq71s0rZozsUv/gFajALL3+k6J2zuQXdz1GfEge0UuVmNbCzlAjL/Vk0fvucs3/4R6H3kX+myPpD4c6pmscGbSZh7i5RrBjJ9/O5xcolcZOnA00Uvi+/qLtw97tmok6OTvfFaZITntVMeEdX38i+0O/tKfqiF4gS9TcPLx+gvAvzWWOoLk8Sj18SyfrbBE/OqTHQf7hmKn09oGoXlsCdHCnq8DeH2tdV2hy4chM3scbEudXKJXGT3pmi9+IX/R+cwcejuXK+XWzpEkzWwmMAygu4Bt+E285xePlx7K27S+KUnoz2n2WccA6RGPMtH6OQGO+jJ8K4SPS73GVgYdcUqIvnTPxxqUJ3ZcUaZz9ZrVwSN2lNnY5vJocF99xwWf+z6UJMMOBojAbQUmXK48BRy+JQy7jRhZe/B8cnb4YkTqnehc8SVXjUscT4dEX/UxlMSM9bnbK63Kv889f+OWKOtbnvvrr+33//82qN8f+rUJGUelzqmNb8NC4nTutEQSDtO4G/aHJOdSRfiJUQ+Fks0xLLs6mw3VshmSjsFZaHn1veLF6/h/mmxDaWKuk0pp9HDc4aZycR1ji0OX9Zgse5S88HkBtrr9dob71g7HVAk7CJxE3ahaDkxOwHDP9Y13OqQh2rR3skt2WWlLyRfK//0P3KCjZWjOua+7+fb16F18yV8yjOUaJ6JXFjo+9ZeKKUU9gfxwb6BMdz6hwb1k3mSj3ZaMLTpWwicZPOW8HffR0Wzny7rnNh2xotU8mLD0taPI0qbfdWSD4Zri9ofPVHj34Pf3aVLvwlkvQpnpxTe98zMW5qurBa4NHNluY+AnL5sXbd9iR52mFCs7CHxI29DuO/UXnjyvmmU4rkzoOx0YlXMlgo6THrreDvZlyI038ldIWW18zd7f4cduHUtPCX6OvX9L2481qiRNieq5uFi4lrm4Mok2DdJGi4IJjjUoiGxE0aklnOY8eTY9ZajFXcRiyWaVtQOUku2Du6/k4aJ3cEtvRxfdiF4+9cm1lf+As+NejGcP9rhdptCrXvmtg3Uo8QJnD31abrKI5LIRoSNzYmpOWF/azSMr/doqwkWcyESyYFStrFNC6kj0BH4GgtIPdj75DA6RS9r1HkMYSdWXGDMxJhtqi7TLagNomy2tJccP3FcSljSNzYCsw+VFzm14n//ykG08ZgPfTCZapd43iiVMkkE67WAnI/VvgjVJqO9sacu0W+wEn05BwNWvqdDQKPbr4NR1ZiGwmWYUtLEhtrN0rmCh+XekfzsIXEja0FBoHZBhO5gmBharBcJdtgCbuYJBdbV3T7ouvP6vjuF7R/ONlLHFMEYmPaSFQiR0wTJsJq3q3R0i9UjVWlK2H3ltRxqXE4SgYjSNzEJ9lBOoq/qMncYiZcclv5pIDFzEHF7b10U8H2ZX1sHy7VnxkKAEjclB2cpS7PmgPvE/pFkf1BqzbnXLXN09kW/w3HpRAFiZv4GoqgGNKT+cjZ23UjHWBqnqBGwu+PxM1u3gr+7lp2S/m7b+alfwjBYwyW72MhEWbAom+cCdTlN4NFuU9rErlnaJcxQWpue0tLsYPETZrgDM69LOA9aljknhlrM53w79e8i0kyadM7nja3i8bJHpOaV1TWPnlT+kXaXEwcNziT6ntcTBy/Ho8EfrXFBFxLixIph12+ROG4FHZG4sbOgk1bGUwLeJ8aJvOR0ELGavAwVrygeVdpnVhwIvi7b11d3/z7zzsr/DNIXUxstZ1IjemMm5GEC4k/Co4pFsuUIzD5777aeozluBRiIHHD4iaFj4WUl5ZFrg8KLSX8LhSUp8a+KVnHXEy8vcbJJqLnFZb5ReHvX6KvdwRncVlLhAk/ieijE7pKwHBC88ChtMfKz4TKieNSRpC4sRdgSJM4v2xhsesXNVaOTEmXaev07bqRTibVGPzH7JuSLios82IDLYFHHRdfZgqDM01rg5hGQn3C7yqW+sY/2Q6HhE8cW9ckjDc1yzk2+IuJ+x1/xiepcirguNQ4jBPvH3lNHKda3AvW5Kb47dkzwd8/deUd+7lSEuT7wcgnvQ6NBF29k00k+rJ8paQ8Wif/GGmTW8UzjWmSdefrrcakW8ntVWphafI+FhJh0dvmPHP9DWsbyfnPquGBBzNXIYEdZN2uP8Dv/lq8b6n1sW8r5wrb74HbPLHr6+IitP2q1rfsuLFF8nHIPsD5WGCZdYreS6lluIp0sOkXixqSiCMFdfrJYds2dFZ5P8LmWqHf21GeUVlMhGU9chaSbpcMCUmdVbzrpi10TKj96VK+vb5fvL6G9fFky7r367O/neAxTAkkbmyRuuh26spNOGhb7Gouy2ELYynJAg3H9s4UTCgE/9uNpRqOL8boR22B5S/1nvsIP0PiYuIYW/i14gldBfarpaSN9Bh6ZbydWHzAxbr2Ch0Taj4u5eMIn7A5iTg2+LjpywbxSdFI3NjzLnOgqDnRUGpg68v0s9Nz5804LMA+u/WfjHTtdDx+WnLheOTkn67WOR4Dvs1C+NLJJ/36CAvFoe9eurISOI1gmZeYaLB8HMRqIkxiXB6Fo0tJLSVtariPQsMxjRPhi6cf1n+zeOUIoku7mPi7cFm21LpMck16ljC28T/zxOlIFidF4iZNoCQddHzO9Ls+Oj1Jm106qsbLP31W+ovwwqcJ9ftlKegbbfCePilpFxID+dTJH7PRUgclaRQFHKcRfsawNbp19wmcEh4Lui/0e3cKwsK3mRKLRstPjbOaCJMK3JIel1CYtEldzlqO1H2W3k0REjZ+zfh9R0XKI1wCd1/1//vvf2Im6T5Y7P/PxIs5doa1znjyhsSN3YVOyh0b4xDMT40s7rQeJWlCOZ9lHoTaMMh+faSO1x34Z4raRs4k2JHTkdC8dZVeWrglDcnS5bqLMS5NV/Ttz6FvHyld3DSCc8uuAXtb6PtWiURYsnEuZTCtbadNX0nf+/6lrcR9Nw8SNtNM42HusTZ2PUvFHU2OXXcPnGWe04edxiaRuLE7iE8STKCNu9+BYWkLrPYntxyFCfG9S/cNw8jdnxO9fGaQXXfC7BUlDpo1PleUhZPTsdPGuXKTNuPMk/wwrmk6nvjB7b4F/6nL6hv348V+raL6l+o/MebuPaH33hldT7WGy7MX+mw+cIs+voZg0NrasKQ1/zB3fskVmPvjWY8kbAb7iT9rTlF3VoWjmFJtJ+eum4mTuYNJw8MlkiBxkyYJoOXRZMNEuuuN2xP39A4MC7QfKRnOb34NAebU7Z7EGZ689HkpgBuv+d81BZbrcOHspYufAHsf6kbTMZQPhfbFoZ7+dmkvmG6Ujmt+/ojxyM51F2fT0Ce+OvkLvY8E+1CMRbRE2cXewq/JXsFt4TnfBMv1JHIAf5RoXo01niYTAvBe0ef1dXAZ6iQ6v6PHJ/4Wr3W+5Es5luc+TtsZijtyzbHST1U9cgYTyS8cUk36raL3Mw0v/74uwp+3Kwaidmngb8LA2FZSZ/Mw+TYFvNfJ0sA7LBqultre7YpgYrQ02W1yT81T72Gd4LILL03tqA1B6jxMnNvuthqH4Hjq9B05mbnyLyUenpZx5O53xd2ENn695YK8Da8DxRN6jN02oy0WZ81SefdL/eM6U13n3k790FWkscVikkGK5USY5Pjsd92cLT7n8Y5BfOP07dj7QbgINkdQP1X0sb+Pp4v68Q+TOF2UwWzHeh7mk4MN5xXfzppEF32PM7ejLlHccSbU/8cZ+oaG49i+fF9bmhRJ3KRbAGqcyMauvm2sm/BByklh77kJr9ztzSeA1t0VcKq0PwwJsCGJeePuk5ndIwGZ7z974Z8bxe3i1FjfHD2yMF5O4PjF4cNvsV+GeoqRrMwSNLo4u212/UatcT8mcbowr3WRA84hOfdOwQJvp4W5wL0By+sNqyTmjeuMfV3S0aLN/rMI3t5vGcifuHofQ72qD06Vrg8/LurrJCQJvo/hTyUmQ90Ou6qHtc54xz48i/mhwlg7Kn1M8AmtxWfphMa5txnGuncK+sCwVu+dESRu0pgXmAAo3W8Rfsa5kgCiBMP9Get8M9k5fbtuHgaPQxLHQr+duXoeAW4tEX3s4mztj7lgatz9rk0X3t91CAKGv99usAgcAoF9p+doYR+hz0iNb1YvJpYqzyyJMP8N/uIzShezf/KP74eH6+yKCAHzO2f3yPwua/6Pit+fH8OHRLwL7e7hrtVUyZADF/++vSIfA/6IT0JzxySsN1LHCBq8S/xZsyJxk66T35IAKC6AG45jsChZf2Bed0L2g+YXiiy5W0sTVGU6F+eS9Cbxwnbk7o+cPdYGr1f8N5qTbDHKXeQ+lkRb+K3M6dqCtFW/S7pf+H78dRHMD0fpe3efxGzcjzsvSlvT3mbqg7eL8ps7XXfcaelfKZISucfalI98l0r6pT4uta+orbfOEC4n1r0QRH6nTs/l0tptMjD7yeGcIkvuA+23SL7ODiP9LOntycuJneGlfWdUjEsiJT6j5fttakiEdYrK27ffE3d/gf9l+Lv/d6m+PR/uFrTQPy6YxlbPBwmOkZrZcROOrUnFiymfLtUqG9vMIHGTNoBCeXrqbm2bfrt06uo5wiPBLy7eUwxFOo7YNyYU58b9ptQnSnExcdnleVVxv/Pj3aGVNUG4AJgvTfLMSW3muu0S/4oLI/UiPX6raTMpkbjRvxjEepqIP+ucCXgtow0HQ47xpHVIERRp5uLdATBxZTwZT5OdE/XW72PJbemCVIl1W05dxf3uMOw2sNSG+dJvtf2IY0NrsI9K7bhpEl2qzzUhCZG4YRC3ImawEvPYgnUHW0xQHJmK79SRKC6Rr7Njwf5Yu97FSZq1gu3Hoiqe0BUSF12F/e50aRdDb+hzsbZ5ZHwMydgSx4brTOPATKhuUhyt1ng0ycxxKRI3ac0cR0OOXZn3/cwd9xStY5utliQZ4vIL4PcUQ3GGBHGs3X2PPTIdT49FMUjdx2J1HG2Ffq9EedZ2N0r34BHkZtbIIQA/dUjZpy1dTKxhHKjlaLWZXUAkbtKreefGsLviU6bfN05QdxyZelrjNt/tdEvZRuMXvW8ohiK9jhwocrfN5kH6TOncs1YAbLhuakqEzSrrc28elLm1dsxR+9ViHZcyt+Mm9IO5ULvxl0ezdigIiZs8i6uuws/du/ukVa6dK7EzqhyZShcw/rSAw1bt8w2LxCIdJlgQvqVYNxLliFo4AtAIBcFWVZMIEz4mkXu+Gu61WfW/mcCum6jrxFVj7ThzfeYcZ6V2+cc+Yt0rjcVNIHGTb5FeU3C1KqDMMSClGNDnTMLJAsbOkRjTFvwjT73FDtR84qClaNd2HnEhJ1XuVi8mbpxMIkyyPD8Z729+Lfj6iSDY1Dy2+JwxxxcrmtC3ta3xNQX7Vo5L9TT3dEjc5OEbcU1P01kVUOYYkFKdYXzv6trOvM1kum3ZzxzJm237GHcwlVlvKcaSKUW7Nj83xUzGjwU/h9X5pKryDMeFrAb6zyVtrLZljoP/rBX+71WPCcaOS/UK43ATSNzkM6sk+H8soMyxKNlP+LOPHbsbnjLZsW+QvJEP/pE4eElYbxyTWr8eYgdU+xKfY7HI743WUa2JsFOj/e31GsdNvln74KF/1vSF7Tp2PZKT++4riV14s0LrRtt4+nAcMjNfkrjJH3B1lQaUfYaOPE7c8V87kjepBv2ZI3mzax+DTn0YO1KN/a2TOVpSohRjuESiwfI8VGUiLOy6sbSLct2kjdn2vPjsfq7mEeH3dt0V31Ywzkodm4y940bTUV5Tu9NJ3OT3xtndFvpcQJl6QBq5tI98I3mTdkKdOS7bfartvXIkbUrThXpLOWaw22b9OSpqPfz651+7HBO1siiOreYndB0bmf98P3u1wcWuZtdUizI4Zt7+7nxRFq93GGubzGOtSDI39JleoH5iH5fSlCy5sNSRSNzIBGCWgv9NjgDkWBy1GT4vAfSKQT9S2c8dybFVi1rKpDynod5SB2ItRf2sVDvVpI71dBYrSTARdqMkyO9d+Uemvs/hmwS94UlMZr+wWXy+mu+k60N72PXYmMnHgD/RhyQcRK53DW3+1rHjBpEa0msDjWkIKLsN/v994veUa3A/dDxtark9v4kYTFwb6R8xzBxJmxLHRZ/cfZ/p99FXnh6bUiba9wTbmEXVJ8LCE4lK7c+ni/f/5pFHftfapod6fePq+8LPr5FfhWOApY0NNT5lLvZxqQ8K2uAHa52KxI18sFtq8L9tQJl6QZLzfPx7l+cbde3t4I8E9Tr0j1qPTg2fX/rJFBxb26ysTl36o1EP9aGtpLxHp0TXGepCItHQbxkYl4BE2J1DV1Yi4/t8tWiX7w3VQXRh500Nd9749eAfvj1EHKv2axkTDB2X6pxsErp3+b5Ay4bEjbwh+O8Leb+7BpSps9ht5vLwA1OKxIV2XWi3qRML81C+s4rKdqaoTQ19nYTA83WWc5fNU32SHTh3wVGOebUVqmerJMpTXSIsvJ9SvrToQpC+65jzzVUgHBmy+oXU9zko7LrqCx8bpMdZqV03se/Mk/zy8Y3FMYTEjZ7B7pXTn4mPEVDOM3TiSeZyGRZZJSXgtl7khoE457f7twK/UzLwlt5ls6rfvw59/7yCNr7N2H2oqFy6MB4NCc+adk0NxyyTX/L6659/tUKf8cZw/dV8MfHDAL93uo/J+v517C+cjZT4SvE5R0rrdh7mDSvrme9rl9AWon+mcPdV1nWugmTuTOj3ThblPYo8TkicTCht1+LaSkvc7Dm7bsNiU+PugtgBZerJal+wnP5QGHinCAYl26G1BE4pn6tfGqNehb/XevfOLJSD5sCqD2PRMCZ1hutj+Kw5gyGp+1hM9jkSYSsD/E3vEcw5/r0K9/FobtdjxXXbh6csaUr6b9MOkiVsBOvxWkP7EHwfkwTlmTN5k+phBCqUlrgZOfuWF9vnwgmAWaKAMvWj2SbCdThbCpb6wtvi+VKAquX4RedsHAmZu3ITUdehbfhA+Xd3l9Q7d7YTOf6zHYfPW1LfvnU/7pqylHBbni9zL9REvkhKHCBJIhG2ur5vQ4Cv4T7ELgTqh7GPwhi+t+m5zz0L8+ipK+MLvz681z9CO8gxHuUea7Ukc6WOSx0k+Jk5no46nH6YWR4zXjhoHhyPw2saOlLr0ievfDB54dIeafI/+2PCz9CERaDkgmwIlvzLJ5LeOvmE0rrtrltqA5p14dWEPvI2/F17+X4IZVtK4L9OW58vtZdR6H9+vNoPfy816X691BcsJDt8mzsPryaMScPcUlp7++RkE563Ar/fypjx1JieO3DuSigYf9Hrr3/+NQtrp1agXk4zlFVX2FgUq279WOLr9zyMySfK1jLDmHsR4S6jEsYGLWvfuUuTRHlOqvXakLzx7fsoQVkdVzBHul8Ke7+XQoO6pnJqw2svBETNjp3IN/KbpSAYaQfDIVDSksS5XQpOOwPB6XipjLVsk+4Mle+2mlAf4zB2NU7nNvY+1NNV+LOvpH5G7j7R1iqsm96Vk1AGkgrHyvwXFdMMwfppgotmsX4dT5zMFx8akjWwvSY8idC+fdv8UFP8SuLGRjk17j6B89i329fufgfN8t8hp3XxknCbJBH8IuymgkTCaCkIzbXzY0iEXS2VL33t+bFreL1c6gcpx/o+vHz9fAt/Ulerx6eX7j7plsvQd25cXQk0YJPgPvaXQX3obwTruup5+EIq5TqmX167hPuVgFzr9IM11xnXS+00x8Nu1CktcfO3k8k8/0LfQqYBbLwUxP72YBBr3OPJnf5BcOMHtn+W/n1P8LNWGT+1KHqujAn801lVL6M1JvlVdUYdba958HrYf56rk8f60JDwZJwCtg/w26Wxcv+JdcNyP7sKf+/YWVNMPQ912oZ/tbc0Pz62ThzG2OHvN0v/7rrWO4agVvvgn1m7FZqQ+JdyAgAAAAAAtSjpqVIN1QUAAAAAAGpC4gYAAAAAAECpkhI3LdUFAAAAAABqUlLi5iXVBQAAAAAAoNNXd3c5scQLAAAAAAAAj2icXNLmkuIHAAAAAAASSjkq1VJVAAAAAACgNqUkbg6oKgAAAAAAUJsSEjejxWsi+PtvaSYAAAAAAEBCCYmbI+Hff0MzAQAAAAAAErQnbvxum3dUEwAAAAAAqJH2xM2Ju0veSOpoJgAAAAAAAD+aOrlHgC+/xlQFAAAAAADAPX+vzb9KXgAAAAAAAHB3u1sunZ6kzReqBAAAAAAASHmh4D00i1e7eL0Nf2rS00QAAAAAAICUHImbM3e3k+Z68fon/Ls9d3fp8NjJXz78lCuaCAAAAAAAsEzT0adNXy3VBwAAAAAApPwfRfCoW8ejwAEAAAAAgCASN4/rKAIAAAAAACCJxM3jLigCAAAAAAAgicTN4zqKAAAAAAAASCJxs1rneBQ4AAAAAAAQRuJmtU8UAQAAAAAAkEbi5mf+aVJzigEAAAAAAEgjcfOzmbtL3gAAAAAAAIgicfOzDxQBAAAAAADQgMTNj2aOS4kBAAAAAIASJG7u+eNRxxQDAAAAAADQgsTNvVPH3TYAAAAAAKAyl4vXv8pfX6gmAAAAAACgDTtu7nbZHFIMAAAAAABAGxI3d/faXFMMAAAAAABAm9oTN/5emxnNAAAAAAAA1ErrHTcfqRoAAAAAAKBZrTtu/E4b7rUBAAAAAADV07Tj5u/Fa0qVAAAAAACAEryo6LN27m6XTU+1AwAAAAAA3JHeccMuGwAAAAAAUCTLO276xevT4nW+eN1S1QAAAAAAAD/LvePm8+I1odgBAAAAAEDpfsnwO8bhtRf+bMIrlm7xul68rhavOVUKAAAAAACs+EXwd/skzmjpT++38M8P+aNON0t/94ma3nHRMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALb0/wIMAFOcMsyvvxAlAAAAAElFTkSuQmCC"
                                                                                         alt="Image"
                                                                                         title="Image"
                                                                                         width="480">
                                                                                </a>

                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <!--[if (gte mso 9)|(IE)]></td>
                                                <![endif]-->
                                                <!--[if (gte mso 9)|(IE)]></td></tr></table>
                                                <![endif]--></td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        <!--[if mso]>
                    </td></tr></table>
                    <![endif]-->
                        <!--[if (IE)]>
                    </td></tr></table>
                    <![endif]-->
                    </td>
                </tr>
                </tbody>
            </table>
            <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top;background-color: transparent"
                   cellpadding="0" cellspacing="0" align="center" width="100%"
                   border="0">
                <tbody>
                <tr style="vertical-align: top">
                    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                        width="100%">
                        <!--[if gte mso 9]>
                    <table id="outlookholder" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td>
                    <![endif]-->
                        <!--[if (IE)]>
                    <table width="500" align="center" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                            <td>
                    <![endif]-->
                        <table class="container"
                               style="border-spacing: 0;border-collapse: collapse;vertical-align: top;max-width: 500px;margin: 0 auto;text-align: inherit"
                               cellpadding="0" cellspacing="0" align="center"
                               width="100%" border="0">
                            <tbody>
                            <tr style="vertical-align: top">
                                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                                    width="100%">
                                    <table class="block-grid"
                                           style="border-spacing: 0;border-collapse: collapse;vertical-align: top;width: 100%;max-width: 500px;color: #333;background-color: transparent"
                                           cellpadding="0" cellspacing="0"
                                           width="100%" bgcolor="transparent">
                                        <tbody>
                                        <tr style="vertical-align: top">
                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;text-align: center;font-size: 0">
                                                <!--[if (gte mso 9)|(IE)]><table width="100%" align="center" bgcolor="transparent" cellpadding="0" cellspacing="0" border="0"><tr>
                                                <![endif]-->
                                                <!--[if (gte mso 9)|(IE)]><td valign="top" width="500">
                                                <![endif]-->
                                                <div class="col num12"
                                                     style="display: inline-block;vertical-align: top;width: 100%">
                                                    <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                           cellpadding="0"
                                                           cellspacing="0"
                                                           align="center"
                                                           width="100%"
                                                           border="0">
                                                        <tbody>
                                                        <tr style="vertical-align: top">
                                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;background-color: transparent;padding-top: 30px;padding-right: 0px;padding-bottom: 30px;padding-left: 0px;border-top: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-left: 0px solid transparent">
                                                                <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                                       cellpadding="0"
                                                                       cellspacing="0"
                                                                       width="100%">
                                                                    <tbody>
                                                                    <tr style="vertical-align: top">
                                                                        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px">
                                                                            <div style="color:#777777;line-height:120%;font-family:'Source Sans Pro', Tahoma, Verdana, Segoe, sans-serif;">
                                                                                <div style='font-size:12px;line-height:14px;font-family:"Source Sans Pro", Tahoma, Verdana, Segoe, sans-serif;color:#777777;text-align:left;'>
                                                                                    <p style="margin: 0;font-size: 14px;line-height: 17px">
                                                                                        <span style="font-size: 16px; line-height: 19px;">We&#8217;d like to&nbsp;extend you an invitation to join us and 200 other hackers on 15th -16th of&nbsp;October at Jacobs University in Bremen, Germany.</span>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 14px;line-height: 16px">
                                                                                        &nbsp;<br>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        <span style="font-size: 16px; line-height: 19px;">It would be great if you can <a
                                                                                                style="color:#0000FF;text-decoration: underline;"
                                                                                                href="https://jacobshack.typeform.com/to/b8Lagp"
                                                                                                target="_blank">let us know</a> if you can make it to the event or not. If&nbsp;you are unable to join for some reason, we can give your spot to other hackers&nbsp;who would like to attend.&nbsp;You can also join the <a
                                                                                                style="color:#0000FF;text-decoration: underline;"
                                                                                                href="https://www.facebook.com/events/277473712613843/"
                                                                                                target="_blank">event on facebook</a> for more updates.<br></span>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        &nbsp;<br>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        <span style="font-size: 16px; line-height: 19px;">Event logistics: Registration opens at 9 AM on 15th October (Saturday) and&nbsp;the opening ceremony starts at 10.30 AM.</span>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        &nbsp;<br>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        <span style="font-size: 16px; line-height: 19px;">We&#8217;ll be sending a Slack invite soon so you can stay in touch with the latest&nbsp;updates about the event.</span>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        &nbsp;<br>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        <span style="font-size: 16px; line-height: 19px;">If you have any questions, feel free to Email us at <a
                                                                                                style="color:#0000FF;text-decoration: underline;"
                                                                                                href="mailto:hello@jacobshack.com?subject=Question regarding jacobsHack! 2016"
                                                                                                target="_blank"
                                                                                                title="hello@jacobshack.com">hello@jacobshack.com</a> or&nbsp;message us on Facebook and Twitter.</span>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        &nbsp;<br>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 16px;line-height: 19px">
                                                                                        <span style="font-size: 16px; line-height: 19px;">If you applied for travel reimbursements, please fill out the <a
                                                                                                style="color:#0000FF;text-decoration: underline;"
                                                                                                href="https://jacobshack.typeform.com/to/oO2rP1"
                                                                                                target="_blank">travel reimbursement form</a> within the next 3 days.<br></span>
                                                                                    </p>
                                                                                </div>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <!--[if (gte mso 9)|(IE)]></td>
                                                <![endif]-->
                                                <!--[if (gte mso 9)|(IE)]></td></tr></table>
                                                <![endif]--></td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        <!--[if mso]>
                    </td></tr></table>
                    <![endif]-->
                        <!--[if (IE)]>
                    </td></tr></table>
                    <![endif]-->
                    </td>
                </tr>
                </tbody>
            </table>
            <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top;background-color: #444444"
                   cellpadding="0" cellspacing="0" align="center" width="100%"
                   border="0">
                <tbody>
                <tr style="vertical-align: top">
                    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                        width="100%">
                        <!--[if gte mso 9]>
                    <table id="outlookholder" border="0" cellspacing="0" cellpadding="0" align="center"><tr><td>
                    <![endif]-->
                        <!--[if (IE)]>
                    <table width="500" align="center" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                            <td>
                    <![endif]-->
                        <table class="container"
                               style="border-spacing: 0;border-collapse: collapse;vertical-align: top;max-width: 500px;margin: 0 auto;text-align: inherit"
                               cellpadding="0" cellspacing="0" align="center"
                               width="100%" border="0">
                            <tbody>
                            <tr style="vertical-align: top">
                                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                                    width="100%">
                                    <table class="block-grid"
                                           style="border-spacing: 0;border-collapse: collapse;vertical-align: top;width: 100%;max-width: 500px;color: #333;background-color: transparent"
                                           cellpadding="0" cellspacing="0"
                                           width="100%" bgcolor="transparent">
                                        <tbody>
                                        <tr style="vertical-align: top">
                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;text-align: center;font-size: 0">
                                                <!--[if (gte mso 9)|(IE)]><table width="100%" align="center" bgcolor="transparent" cellpadding="0" cellspacing="0" border="0"><tr>
                                                <![endif]-->
                                                <!--[if (gte mso 9)|(IE)]><td valign="top" width="500">
                                                <![endif]-->
                                                <div class="col num12"
                                                     style="display: inline-block;vertical-align: top;width: 100%">
                                                    <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                           cellpadding="0"
                                                           cellspacing="0"
                                                           align="center"
                                                           width="100%"
                                                           border="0">
                                                        <tbody>
                                                        <tr style="vertical-align: top">
                                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;background-color: transparent;padding-top: 25px;padding-right: 0px;padding-bottom: 25px;padding-left: 0px;border-top: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-left: 0px solid transparent">
                                                                <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                                       width="100%"
                                                                       border="0"
                                                                       cellspacing="0"
                                                                       cellpadding="0">
                                                                    <tbody>
                                                                    <tr style="vertical-align: top">
                                                                        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                                                                            align="center"
                                                                            valign="top">
                                                                            <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                                                   border="0"
                                                                                   cellspacing="0"
                                                                                   cellpadding="0">
                                                                                <tbody>
                                                                                <tr style="vertical-align: top">
                                                                                    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;text-align: center;padding-top: 10px;padding-right: 10px;padding-bottom: 10px;padding-left: 10px;max-width: 119px"
                                                                                        align="center"
                                                                                        valign="top">

                                                                                        <!--[if (gte mso 9)|(IE)]>
            <table width="94" align="left" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td align="left">
            <![endif]-->
                                                                                        <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                                                               width="100%"
                                                                                               align="left"
                                                                                               cellpadding="0"
                                                                                               cellspacing="0"
                                                                                               border="0">
                                                                                            <tbody>
                                                                                            <tr style="vertical-align: top">
                                                                                                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                                                                                                    align="left"
                                                                                                    valign="middle">


                                                                                                    <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top;padding: 0 5px 5px 0"
                                                                                                           align="left"
                                                                                                           border="0"
                                                                                                           cellspacing="0"
                                                                                                           cellpadding="0"
                                                                                                           height="37">
                                                                                                        <tbody>
                                                                                                        <tr style="vertical-align: top">
                                                                                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                                                                                                                width="37"
                                                                                                                align="left"
                                                                                                                valign="middle">
                                                                                                                <a href="https://www.facebook.com/jacobshack.bremen/?fref=ts"
                                                                                                                   title="Facebook"
                                                                                                                   target="_blank">
                                                                                                                    <img style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block;border: none;height: auto;line-height: 100%;max-width: 32px !important"
                                                                                                                         src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA0pJREFUWAnFV01IVFEUPve+GW3U0ZpQzAINyiDITQYui4hMIXCRi4TauClwUaugMEtcRBBEYBFtXCRkkBSkYVAEgQNBUIugCDSIydIUndTyzZvX/e7MffPm970ZdLyg997z95059+97jFy2U30jJeFv+pEoYydZlPYLtzqTUR3cmUkh0YVMTp+4aT7z13tfP+7rXIPOqTEng7bzI7XGqtFLZrTLJKp0sodeBF0ixh9qPu362GDnTC6frAmc6BkrjYYXL5sUvSgClOcKkkO3zIjf4v6qgfE7bf8y2WVMAL86sqKPCoeWTE4FyIKeMm9HpmqkJdDaPdxkGuZz06RdBQBldWGMvjONtb94cPqj3Sgpgdh66+/WG1wBIgnN5z1krwRXSqw5yr5R4MBBbGAAS+F61AAbTozzWvPG3QE629FEe+oD5K8oobU1g0YnPtPQaFKVFYTqW+JYvRDICqD08d2ujBz7pn01dPvKcWo+sIO2VpaSxhn5tniorMzr6AssYMJQJmCs6FfFOK+jdq7rIHFrAR0xUw3K5d0ipAw33NK0Puv2kkGk0hKNnt7rJLGpZJt4O0VDTz7Qyt8I6bpBeiQaU+T4L1yXKhu81R5cr/mAI2bN9nILHPPxN19pbmEVQ9cNmMDmuNtde8UNufrp8blhiHAFNGB78LC4dcfGQ6utrkiC29sQkMsCYehX2HU1gI1jKF+0pIhZJjcvHc2o6TnTbMlv3J+kV5PT1txhUMfVk+pg6Fo9M/vHtS2wCz9IWWBm5pazaNLFTNyNHpAJsQca09XpkvbuR1JYv7OKBq+1WgYXBl7Sl6l5OY8YzkfQcjTZD1QAbMZVQ3D5l3LOcQqUzlWghFGIg0Yl5sUdSQoHDldc2AQasDkIJK7FhLg4I2ACm0v2KghkcWBtKAIT2PIYgr0KlfvzY4tT4HA5jhl7jkGRwF4LDJa3G7AULbMYEaizEV44JqI5sqL5xVW6O/zeAv75O6/iBYGlnOMvemy6qaQUKcilENQZ7FVluF49YoKWq9KruGlvAXg7qLMwCCqjdeiDiJn6TYC4aQlAiCw1/7bDYrP0i2leCwx/W8OnWT9ipf5yZZO0B5TQ3sf2xSZ8nNqTwHijPs//A01CT3sm1mNYAAAAAElFTkSuQmCC"
                                                                                                                         alt="Facebook"
                                                                                                                         title="Facebook"
                                                                                                                         width="32">
                                                                                                                </a>
                                                                                                            </td>
                                                                                                        </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                    <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top;padding: 0 5px 5px 0"
                                                                                                           align="left"
                                                                                                           border="0"
                                                                                                           cellspacing="0"
                                                                                                           cellpadding="0"
                                                                                                           height="37">
                                                                                                        <tbody>
                                                                                                        <tr style="vertical-align: top">
                                                                                                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top"
                                                                                                                width="37"
                                                                                                                align="left"
                                                                                                                valign="middle">
                                                                                                                <a href="https://twitter.com/jacobs_hack"
                                                                                                                   title="Twitter"
                                                                                                                   target="_blank">
                                                                                                                    <img style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block;border: none;height: auto;line-height: 100%;max-width: 32px !important"
                                                                                                                         src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA89JREFUWAnFV91rE0EQ/+3lTJO2pk1r7QcqUouaFn2y6IugFUQsKCoVxb+hiIJPokKLgiC++CL4rIIifqEiUi0IIogoxdYPilWU2tovbZomTc+sM5fc5XK5XFJtdeHY3ZnZ+c3NzM3OCRQ42nqlV7yd3Aohd0kpG4VAHc11fFwIMSglBmnugxR3ZCjw5HqTiBeiWuQTars3VYNY/KSQOCSBQD555pPSSSlwGT5vx/XW0iG3MzkNaL8vi4ajP45DyqMEXOKmJBePlEfIPeer/eWnL+wUM05yjgbwW4tY/Ca5dZPTobnSKFzPpc+7x8kbWQYcvD2+XtNwDxLL5grkKi/wVVXRenV3RY9VLsOAVLxfzDu4gUhGUF40Wz2hGDyOObt9wcAZiLzKGIxl4JoGcMLNV8wN5U4zY+jJnWLqIdCTLhrv/9NsdwJyoxFoRPq9DRwK3QMiGj/1N+BlRQItK71oC/mwoXaRib2kWIFPNbfmQsei2sIEkaxwEyNEdCwye9f6MB5NoPuzc2Fbt1TFkY0lKPWa0cT7MQ0xTaJxiYrDDycxSuftg7wwKUPBKpXLay5wPrR5uRe1ixVU+BXcfh/DLxI2RrEq0N6cCc68NZXJ1w7PJLB9VRGuvIkaR8yZMRlb4dpuUh0WCpmqUCU50OTH2W0BNAQ9plSoSkW5L/3mJiO1+DkjcfdDzE5O7wlb5YslTcle9Y5q5IEk6IoyD860BPDph4aeYQ0cY7fR+TSMcNziMpswY6vJW83GsWxrSrJBVpar4MdtzFKsJmK5wfksYyvGlZpLWU1p2uW5ZJzoYw6JZ5dj7OzXs0ndfJedQDYRx23Pd82RnkEUkJRfYjCDaNs8Goija8DxJrVJZm6ffXH+bK1SAuIbhQCuBvCB0ens79iqyL5+PTSLPkrefIOx2QN9+QRv0ff/cSK/QtbDBejSq+l8KnU+Yyvcw+WT5uJzsjuMx5/cQ6ElJC6+jGCkUI8RtmspXl3hQX1QRSVVwQZaN1Wl67zd6Eg8gXPPI+gdKcxTRilWuHvVG0i7RtqP03dcT5VvB5XTXODs8gf9MRzrChcMzlCMydhkCJDvOuYbrbnWi2UBBVXFHmiUPcNTCQxN/cIrqojTs+4FhzGsg0DN61g3gJn7b0x0UGE4YRVcqDUlX+e1fUH9OjYLEbfO3L0uFKihlzEYy9wbC57/a1PKBnCLxK0z/dp85f28jlRbbu2IWb+ZA1YwPSn/0Y+JmQNWA9jKan9wCycLZ6yVN5c1n2UdrMv+5oYeRw8YTJ5TefHvf06tRuiGLNDv+W/sBp2eY7Wv7wAAAABJRU5ErkJggg=="
                                                                                                                         alt="Twitter"
                                                                                                                         title="Twitter"
                                                                                                                         width="32">
                                                                                                                </a>
                                                                                                            </td>
                                                                                                        </tr>
                                                                                                        </tbody>
                                                                                                    </table>

                                                                                                </td>
                                                                                            </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                        <!--[if (gte mso 9)|(IE)]>
                </td>
              </tr>
            </table>
            <![endif]-->
                                                                                    </td>
                                                                                </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody>
                                                                </table>
                                                                <table style="border-spacing: 0;border-collapse: collapse;vertical-align: top"
                                                                       cellpadding="0"
                                                                       cellspacing="0"
                                                                       width="100%">
                                                                    <tbody>
                                                                    <tr style="vertical-align: top">
                                                                        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-top: 10px;padding-right: 10px;padding-bottom: 10px;padding-left: 10px">
                                                                            <div style="color:#bbbbbb;line-height:120%;font-family:'Source Sans Pro', Tahoma, Verdana, Segoe, sans-serif;">
                                                                                <div style="font-size:12px;line-height:14px;color:#bbbbbb;font-family:'Source Sans Pro', Tahoma, Verdana, Segoe, sans-serif;text-align:left;">
                                                                                    <p style="margin: 0;font-size: 18px;line-height: 22px;text-align: center">
                                                                                        <a style="color:#C7702E;text-decoration: underline;"
                                                                                           href="https://www.google.de/maps/place/Jacobs+University+Bremen/@53.1677169,8.6520767,17z/data=!3m1!4b1!4m5!3m4!1s0x47b12ca1e7c06c65:0x903fa1786c3fd4e9!8m2!3d53.1677169!4d8.6542654"
                                                                                           target="_blank"><span
                                                                                                style="font-size: 14px; line-height: 16px;">Jacobs University Bremen</span></a>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 18px;line-height: 21px;text-align: center">
                                                                                        <span style="font-size: 14px; line-height: 16px;">Campus Ring 1</span>
                                                                                    </p>
                                                                                    <p style="margin: 0;font-size: 18px;line-height: 21px;text-align: center">
                                                                                        <span style="font-size: 14px; line-height: 16px;">28759 - Bremen, Germany</span>
                                                                                    </p>
                                                                                </div>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <!--[if (gte mso 9)|(IE)]></td>
                                                <![endif]-->
                                                <!--[if (gte mso 9)|(IE)]></td></tr></table>
                                                <![endif]--></td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        <!--[if mso]>
                    </td></tr></table>
                    <![endif]-->
                        <!--[if (IE)]>
                    </td></tr></table>
                    <![endif]-->
                    </td>
                </tr>
                </tbody>
            </table>
        </td>
    </tr>
    </tbody>
</table>


</body>
</html>
"""


def email_body(recepient_name):
    return _EMAIL_BODY.format(recepient_name)

def send_email(sender, recepient, recepient_name):
    mail = Mail(sender, _SUBJECT, recepient, Content("text/plain", email_body(recepient_name)))
    mail.add_content(Content("text/html", _EMAIL_HTML))
    resoponse = _SENDGRID.client.mail.send.post(request_body=mail.get())
    return resoponse

if __name__ == '__main__':
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeform_viz.settings")

    import django

    django.setup()

    from typeform_viz.models import JHAPP
    apps_to_email = JHAPP.apps.get_accepted_but_not_emailed()
    for app in apps_to_email:
        try:
            resoponse = send_email(Email(_SENDER), Email(app.email), app.first_name)
            if resoponse._status_code == 202:
                print("Sent email to {}".format(app.email))
                app.sentmail = True
            else:
                app.sentmail = False
                print("Can't send email to {}".format(app.email))
            app.save()
        except:
            app.sentmail = False
            print("Can't send email to {}".format(app.email))
            app.save()
