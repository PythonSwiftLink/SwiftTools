from swift_types import *


@python
class DocumentType:

    """
    https://developer.apple.com/documentation/uniformtypeidentifiers/system_declared_uniform_type_identifiers
    """
    #text
    xml = "xml"
    rtf = "rtf"
    yaml = "yaml"
    json = "json"
    vCard = "vCard"
    text = "text"
    plainText = "plainText"
    utf8PlainText = "utf8PlainText"
    utf16PlainText = "utf16PlainText"
    utf16ExternalPlainText = "utf16ExternalPlainText"

    delimitedText = "delimitedText"
    commaSeperatedText = "commaSeperatedText"
    tabSeperatedText = "tabSeperatedText"
    utf8TabSeperatedText = "utf8TabSeperatedText"
    
    url = "url"
    fileURL = "fileURL"
    item = "item"
    content = "content"
    data = "data"
    bundle = "bundle"
    log = "log"


    spreadsheet = "spreadsheet"
    presentation = "presentation"
    database = "database"
    message = "message"
    contact = "contact"
    calenderEvent = "calenderEvent"
    toDoItem = "toDoItem"
    emailMessage = "emailMessage"
    font = "font"

    image = "image"
    audio = "audio"
    audiovisualContent = "audiovisualContent"
    movie = "movie"
    video = "video"



    zip = "zip"
    gzip = "gzip"
    bz2 = "bz2"
    appleArchive = "appleArchive"

    #images
    ico = "ico"
    icns = "icns"
    png = "png"
    jpeg = "jpeg"
    webP = "webP"
    tiff = "tiff"
    bmp = "bmp"
    svg = "svg"
    rawImage = "rawImage"


    #ebook
    pdf = "pdf"
    epub = "epub"

    #audio
    mp3 = "mp3"
    wav = "wav"
    aiff = "aiff"
    midi = "midi"
    mpeg4Audio = "mpeg4Audio"

    #video

    avi = "avi"
    mpeg = "mpeg"
    mpeg4Movie = "mpeg4Movie"



@swift_object
class DocumentPicker:

    def __init__(self, did_pick_callback: object, did_cancel_callback: object) -> None:...
        
    def pick(self, types: list[str]):...

    def export(self, files: list[str]):...
    