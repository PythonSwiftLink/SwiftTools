//
//  CVPixelBuffer+PyPointer.swift
//  test
//
//  Created by MusicMaker on 29/12/2022.
//

import Foundation
import AVFoundation

fileprivate extension UnsafeMutablePointer<Int> {
    init(_ value: Int) {
        self = .allocate(capacity: 1)
        self.pointee = value
    }
}
fileprivate extension UnsafeMutablePointer<CChar> {
    static let ubyte_format: Self = makeCString(from: "B")
}

fileprivate extension Int {
    var stride: UnsafeMutablePointer<Int> {
        let _stride = UnsafeMutablePointer<Int>.allocate(capacity: 1)
        _stride.pointee = self
        return _stride
    }
}

extension CVPixelBuffer: PyBufferProtocol, PyConvertible {
    public var pyObject: PythonObject {
        _create_pyCVPixelBuffer(self)
    }
    
    public var pyPointer: PyPointer {
        create_pyCVPixelBuffer(self)
    }
    
    public func __buffer__(s: PyPointer, buffer: UnsafeMutablePointer<Py_buffer>) -> Int32 {
        let element_size = MemoryLayout<UInt8>.size
        
        CVPixelBufferLockBaseAddress(self, [])

        let size = CVPixelBufferGetDataSize(self)
        guard let pixel_buf = CVPixelBufferGetBaseAddress(self) else {
            PyErr_SetString(PyExc_MemoryError, "CVPixelBuffer has no buffer")
            return -1
        }
        buffer.pointee.obj = s
        buffer.pointee.buf = pixel_buf
        
        buffer.pointee.len = size
        buffer.pointee.readonly = 0
        buffer.pointee.itemsize = element_size
        buffer.pointee.format = .ubyte_format
        buffer.pointee.ndim = 1
        buffer.pointee.shape = size.stride
        buffer.pointee.strides = element_size.stride
        
        buffer.pointee.suboffsets = nil
        buffer.pointee.internal = nil
        
        CVPixelBufferUnlockBaseAddress(self, [])
        
        return 0
    }
}
