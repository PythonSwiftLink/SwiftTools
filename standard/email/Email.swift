//
//  Email.swift
//  qwerty
//
//  Created by MusicMaker on 31/07/2022.
//

import Foundation
import MessageUI


class Email: NSObject {
    
    let handler: MFMailComposeViewController
    
    override init() {
        handler = .init()
        super.init()
        
        handler.mailComposeDelegate = self
    }
    
    
    
}

extension Email: MFMailComposeViewControllerDelegate {
    func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
        
    }
}

extension Email: Email_PyProtocol {
    func set_cc_recipients(recipients: [String]) {
        handler.setCcRecipients(recipients)
    }
    
    func set_bcc_recipients(recipients: [String]) {
        handler.setBccRecipients(recipients)
    }
    
    func set_to_recipients(recipients: [String]) {
        handler.setToRecipients(recipients)
    }
    
    func set_body(body: String, html: Bool) {
        handler.setMessageBody(body, isHTML: true)
    }
    
    func set_subject(subject: String) {
        handler.setSubject(subject)
    }
    
    func set_title(title: String) {
        handler.title = title
    }
    
    func add_attachment(image_data: PythonPointer, filename: String) {
        guard let data: Data = image_data.bytesAsData() else { return }
        handler.addAttachmentData(data, mimeType: "public.data", fileName: filename)
    }
    
    func send() {
        showPopup(view: handler)
    }
    
    
    
}
