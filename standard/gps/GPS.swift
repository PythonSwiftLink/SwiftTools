//
//  GPS.swift
//  test
//
//  Created by MusicMaker on 06/01/2023.
//

import Foundation
import CoreLocation



class GPS: NSObject {
    
    var on_location: PyPointer = nil
    var on_status: PyPointer = nil
    
    let location_manager: CLLocationManager
    
    override init() {
        
        location_manager = .init()
        
        super.init()
    }
    
    
}


extension GPS: GPS_PyProtocol {
    func configure(on_location: PythonPointer, on_status: PythonPointer) {
        self.on_location = on_location.isNone ? nil : on_location
        self.on_status = on_status.isNone ? nil : on_status
    }
    
    func start(minTime: Int, minDistance: Int) {
        location_manager.delegate = self
        location_manager.requestWhenInUseAuthorization()
        location_manager.startUpdatingLocation()
    }
    
    func stop() {
        location_manager.stopUpdatingLocation()
    }
    
    
}
extension CLLocation {
    
    var latitude: CLLocationDegrees { coordinate.latitude }
    var longitude: CLLocationDegrees { coordinate.longitude }
}


extension GPS: CLLocationManagerDelegate {
    
    func handleStatus(status: CLAuthorizationStatus) {
        guard on_status != nil else { return }
        
        var provider_status = ""
        var s_status = ""
        switch status {
        case .notDetermined:
            provider_status = "provider-disabled"
            s_status = "notDetermined"
        case .restricted:
            provider_status = "provider-enabled"
            s_status = "restricted"
        case .denied:
            provider_status = "provider-disabled"
            s_status = "denied"
        case .authorizedAlways:
            provider_status = "provider-enabled"
            s_status = "authorizedAlways"
        case .authorizedWhenInUse:
            provider_status = "provider-enabled"
            s_status = "authorizedWhenInUse"
        case .authorized:
            provider_status = "provider-enabled"
            s_status = "authorized"
        @unknown default:
            provider_status = "provider-disabled"
            s_status = "@unknown"
        }
        on_status([
            provider_status.pyPointer,
            "\(s_status): standard-ios-provider".pyPointer
        ])
    }
    
    @available(iOS 14.0, *)
    func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
        handleStatus(status: manager.authorizationStatus)
    }
    
    
        
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        handleStatus(status: status)
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard on_location != nil, let location = manager.location else { return }
        
        let coord = location.coordinate
        
        on_location([
            coord.latitude.pyPointer,
            coord.longitude.pyPointer,
            location.speed.pyPointer,
            location.course.pyPointer,
            location.altitude.pyPointer,
            manager.desiredAccuracy.pyPointer
        ])
    }
}


