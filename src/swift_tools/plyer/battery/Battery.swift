//
//  Battery.swift
//

import Foundation
import UIKit


class Battery {
    
    let device = UIDevice.current
    
    var state: PyPointer {
        
        if !device.isBatteryMonitoringEnabled {
            device.isBatteryMonitoringEnabled = true
        }
        var isCharging: PyPointer
        
        switch device.batteryState {
        case .unknown:
            isCharging = .False
        case .unplugged:
            isCharging = .False
        case .charging:
            isCharging = .True
        case .full:
            isCharging = .False
        @unknown default:
            isCharging = .False
        }
        let procentage = (device.batteryLevel * 100).pyPointer
        
        let status = PyDict_New()
        PyDict_SetItem(status, "isCharging", isCharging)
        PyDict_SetItem(status, "procentage", procentage)
        return status
    }
    
}
extension Battery: Battery_PyProtocol {
    
    func get_state() -> PythonPointer {
        state
    }
    
    
}

extension UIDevice.BatteryState: PyConvertible, ConvertibleFromPython {
    public var pyObject: PythonObject {
        .init(getter: rawValue.pyPointer)
    }
    
    public var pyPointer: PyPointer {
        rawValue.pyPointer
    }
    
    public init(_ object: PythonObject) {
        self = .init(rawValue: .init(object)) ?? .unknown
    }
    
    public init?(_ ptr: PyPointer) {
        self.init(rawValue: .init(ptr) ?? 0)
    }
    
    public init(object: PyPointer) throws {
        guard let value = Self.init(rawValue: try .init(object: object)) else { throw PythonError.long }
        self = value
    }
}

class BatteryAdvanced: NSObject, BatteryAdvanced_PyProtocol {
    
    let device = UIDevice.current
    
    var py_callback: BatteryAdvancedPyCallback? = nil
    
    override init() {
        super.init()
        
        NotificationCenter.default.addObserver(self, selector: #selector(self.batteryLevelChanged), name: UIDevice.batteryLevelDidChangeNotification, object: nil)
        NotificationCenter.default.addObserver(self, selector: #selector(self.batteryStateChanged), name: UIDevice.batteryStateDidChangeNotification, object: nil)
    }
    
    @objc func batteryLevelChanged(notification: NSNotification) {
        py_callback?.batteryLevelChanged(level: .init(device.batteryLevel))
    }
    
    @objc func batteryStateChanged(notification: NSNotification) {
        py_callback?.batteryStateChanged(state: device.batteryState.rawValue)
    }
    
    deinit {
        NotificationCenter.default.removeObserver(self)
    }
}
