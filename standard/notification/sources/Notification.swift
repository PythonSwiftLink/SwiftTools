//
//  Notification.swift
//  untitled
//
//  Created by MusicMaker on 26/12/2022.
//

import Foundation
import NotificationCenter


class Notification {
    
    init() {
    }
    
    func requestAuthorization(completion: @escaping  (Bool) -> Void) {
        UNUserNotificationCenter.current()
            .requestAuthorization(options: [.alert, .sound]) { granted, _  in
                // TODO: Fetch notification settings
                completion(granted)
            }
    }
    
}

extension Notification: Notification_PyProtocol {
    func increase_badge_count(count: Int) {
        UNUserNotificationCenter.current().requestAuthorization(options: .badge) { (granted, error) in
            if let error = error {
                print(error.localizedDescription)
                return
            }
            if granted {
                DispatchQueue.main.async {
                    UIApplication.shared.applicationIconBadgeNumber += count
                }
            }
        }
        

    }
    
    func reset_bagde_count() {
        UNUserNotificationCenter.current().requestAuthorization(options: .badge) { (granted, error) in
            if let error = error {
                print(error.localizedDescription)
                return
            }
            if granted {
                DispatchQueue.main.async {
                    UIApplication.shared.applicationIconBadgeNumber = 0
                }
            }
        }
    }
    
    func new_notification(title: String, message: String, timing: TimeInterval, id: String, should_repeate: Bool) {
        
        
        requestAuthorization { granted in
            if granted {
                print("Success")
                let content = UNMutableNotificationContent()
                content.title = title
                content.body = message
                
                let trigger = UNTimeIntervalNotificationTrigger(
                    timeInterval: timing,
                    repeats: should_repeate
                )
         
                let request = UNNotificationRequest(
                    identifier: id,
                    content: content,
                    trigger: trigger
                )
                // 5
                UNUserNotificationCenter.current().add(request) { error in
                    if let error = error {
                        print(error)
                        return
                    }
                    print("added event with id: \(id)")
                }
                
            }
            else {
                print("Failed")
            }
        }
        
    }
    
    func remove_notification(id: String) {
        UNUserNotificationCenter.current()
            .removePendingNotificationRequests(withIdentifiers: [id])
    }
    
    
}
