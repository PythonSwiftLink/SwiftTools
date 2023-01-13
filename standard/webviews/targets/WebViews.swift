//
//  WebViewScreen.swift
//  test
//
//  Created by MusicMaker on 08/01/2023.
//

import Foundation

import WebKit
import UIKit

fileprivate let retinaScale = 1.0 / UIScreen.main.nativeScale
fileprivate let screen_size = UIScreen.main.nativeBounds


fileprivate func invertedHeight(_ v: Double) -> Double {
    var result: Double = 0
    let o = UIDevice.current.orientation
    if o.isLandscape {
        result = screen_size.width - v
    } else if o.isLandscape {
        result = screen_size.height - v
    }
//    if o.isFlat {
//        fatalError()
//    }
//    switch UIDevice.current.orientation {
//    case .landscapeLeft, .landscapeRight:
//        result = screen_size.width - v
//    case .portrait, .portraitUpsideDown:
//        result = screen_size.height - v
//   default:
//        result = 0
//    }
    print("invertedHeight:",result, "isFlat",UIDevice.current.orientation.isFlat)
    return result
}

fileprivate extension Double {
    var retinaScaled: Self { self * retinaScale }
}


class WebViewer {
    
    let view = WKWebView()
    var frame: CGRect = UIScreen.main.bounds
    var viewcontroller: UIViewController?
}

extension WebViewer: WebViewer_PyProtocol {
    
    var can_go_forward: Bool { view.canGoForward}
    
    var can_go_back: Bool { view.canGoBack}
    
    func set_frame(x: Double, y: Double, w: Double, h: Double) {
        print(self,x,y,w,h)
        view.frame = .init(x: x.retinaScaled, y: y.retinaScaled, width: w.retinaScaled, height: h.retinaScaled)
    }
    
    func show() {
        guard let kivy_vc = get_viewcontroller() else { return }
        kivy_vc.view.addSubview(view)
    }
    
    func present() {
        viewcontroller = .init()
        guard let kivy_vc = get_viewcontroller(), let vc = viewcontroller else { return }
        vc.view = view
        kivy_vc.present(vc, animated: true)
    }
    
    func dismiss() {
        
        if viewcontroller != nil {
            viewcontroller?.dismiss(animated: true)
            viewcontroller = nil
            return
        }
        
        view.removeFromSuperview()
        
    }
    
    func reload() {
        view.reload()
    }
    
    func reloadFromOrigin() {
        view.reloadFromOrigin()
    }
    
    func forward() {
        view.goForward()
    }
    
    func back() {
        view.goBack()
    }
    
    func load_data(data: Data, mime: String, char_encoing: String, base_url: String) {
        view.load(data, mimeType: mime, characterEncodingName: char_encoing, baseURL: .init(string: base_url)!)
    }
    
    func load_url(url: String) {
        
        DispatchQueue.global().async {
            guard let url = URL(string: url) else { return }
            let request = URLRequest(url: url)
            DispatchQueue.main.async { [weak self] in
                self?.view.load(request)
            }
        }
        
    }
    
    func load_html_string(string: String, base_url: String) {
        let base: URL? = base_url != "" ? .init(string: base_url) : nil
        view.loadHTMLString(string, baseURL: base)
    }
    
    
}


class JavaViewer {
    
    let view = WKWebView()
    var frame: CGRect = UIScreen.main.bounds
    var viewcontroller: UIViewController?
    
    
}

extension JavaViewer: JavaViewer_PyProtocol {
    func load_html(html: String) {
        DispatchQueue.global().async {
            DispatchQueue.main.async { [weak self] in
                self?.view.loadHTMLString(html, baseURL: nil)
            }
        }
    }
    
    func evaluate_javascript(js: String) {
        DispatchQueue.global().async {
            DispatchQueue.main.async { [weak self] in
                self?.view.evaluateJavaScript(js)
            }
        }
        
    }
    
    func set_frame(x: Double, y: Double, w: Double, h: Double) {
        print("set frame:",x,y,w,h)
        view.frame = .init(x: x.retinaScaled, y: y.retinaScaled, width: w.retinaScaled, height: h.retinaScaled)
    }
    
    func show() {
        guard let kivy_vc = get_viewcontroller() else { return }
        //view.frame = frame
        kivy_vc.view.addSubview(view)
    }
    
    func present() {
        viewcontroller = .init()
        guard let kivy_vc = get_viewcontroller(), let vc = viewcontroller else { return }
        vc.view = view
        kivy_vc.present(vc, animated: true)
    }
    
    func dismiss() {
        
        if viewcontroller != nil {
            viewcontroller?.dismiss(animated: true)
            viewcontroller = nil
            return
        }
        
        view.removeFromSuperview()
        
    }
    
    func reload() {
        view.reload()
    }
}
