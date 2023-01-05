//
//  TestBuffer.swift
//  test
//
//  Created by MusicMaker on 28/12/2022.
//

import Foundation
import AVFoundation


fileprivate let fill_Py_Buffer_format: UnsafeMutablePointer<CChar> = makeCString(from: "B")


fileprivate extension UnsafeMutablePointer<Int> {
    init(_ value: Int) {
        self = .allocate(capacity: 1)
        self.pointee = value
    }
}
fileprivate extension UnsafeMutablePointer<CChar> {
    static let ubyte_format: Self = makeCString(from: "B")
}

extension Data: PyBufferStructProtocol {
    
    
    mutating public func __buffer__(s: PyPointer, buffer: UnsafeMutablePointer<Py_buffer>) -> Int32 {
        let element_size = MemoryLayout<UInt8>.size
        let size = count
        //var shape = size
        self.withUnsafeMutableBytes { data_buf in

            buffer.pointee.obj = s
            buffer.pointee.buf = data_buf.baseAddress

            buffer.pointee.len = size
            buffer.pointee.readonly = 0
            buffer.pointee.itemsize = element_size
            buffer.pointee.format = .ubyte_format
            buffer.pointee.ndim = 1
            buffer.pointee.shape = .init(size)
            buffer.pointee.strides = .init(element_size)

            buffer.pointee.suboffsets = nil
            buffer.pointee.internal = nil
        }
        return 0
    }



}


extension Array where Element == UInt8 {
    
    public mutating func fill_PyBuffer(s: PyPointer, buf: UnsafeMutablePointer<Py_buffer>) -> Int32 {
        let element_size = MemoryLayout<UInt8>.size
        let size = count
        //var shape = size
        self.withUnsafeMutableBytes { arr_buf in
            
            buf.pointee.obj = s
            buf.pointee.buf = arr_buf.baseAddress
            
            buf.pointee.len = size
            buf.pointee.readonly = 0
            buf.pointee.itemsize = element_size
            buf.pointee.format = .ubyte_format
            buf.pointee.ndim = 1
            buf.pointee.shape = .init(size)
            buf.pointee.strides = .init(element_size)
            //
            buf.pointee.suboffsets = nil
            buf.pointee.internal = nil
        }
        return 0
    }

    
    
    @inlinable
    mutating func withMemoryView_(_ completion: @escaping (PythonPointer)->Void ) -> Void {
        let size = self.count //* uint8_size
        self.withUnsafeMutableBytes { buffer in
            var pybuf = Py_buffer()
            PyBuffer_FillInfo(&pybuf, nil, buffer.baseAddress, size , 0, PyBUF_WRITE)
            pybuf.format = nil
            guard let view = PyMemoryView_FromBuffer(&pybuf) else { return }
            completion(view)
            //PyBuffer_Release(&pybuf)
            Py_DecRef(view)
        }
    }
    
}

class TestBuffer {
    var array: [UInt8]
    
    init() {
        //array = .init(repeating: 255, count: 1920*1080*3)
        self.array = []
        for _ in 0..<(1920*1080) {
            array.append(contentsOf: [255,0,0,255])
        }
    }
}

extension TestBuffer: TestBuffer_PyProtocol {
    func __getitem__() -> UInt8 {
        return 0
    }
    
    func __setitem__(value: UInt8) {
        
    }
    
    func __len__() {
        
    }
    
    
    // called on memoryview(this) bytes(this) and as blit_buffer source
    func __buffer__(s: PyPointer, buffer: UnsafeMutablePointer<Py_buffer>) -> Int32 {
        return array.fill_PyBuffer(s: s, buf: buffer)
    }
    
    
}
