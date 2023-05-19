

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5

ApplicationWindow{
    visible: true
    width: 1920
    height: 1080
    title: "Vbite Flasher"
    
    Rectangle {
    width: 1920
    height: 1080
    color: "#0c1012"
    radius: 0

    Text {
        width: 278
        height: 54
        color: "#ffffff"
        text: qsTr("Vbite Flasher")
        font.family: "Verdana"
        font.pointSize: 42
        minimumPixelSize: 19
        minimumPointSize: 27
        anchors.verticalCenterOffset: -456
        anchors.horizontalCenterOffset: 0
        anchors.centerIn: parent
    }

    Image {
        id: favicon
        x: 100
        y: 41
        width: 90
        height: 86
        source: "images/favicon.icns"
        fillMode: Image.PreserveAspectFit
    }

    ComboBox {
        id: combobox
        x: 100
        y: 297
        width: 824
        height: 68
        state: "Seleziona una board..."
    }

    Text {
        id: text1
        x: 100
        y: 239
        width: 824
        height: 52
        color: "#ffffff"
        text: qsTr("Seleziona la Board per la programmazione:")
        font.pixelSize: 30
        verticalAlignment: Text.AlignVCenter
        font.family: "Verdana"
    }

    Button {
        id: flash_button
        x: 992
        y: 297
        width: 799
        height: 68
        text: qsTr("Flash")
        highlighted: false
        spacing: 8
        font.family: "Verdana"
        icon.source: ""
        flat: false
        icon.color: "#ff7175"
        font.pointSize: 30
    }

    TextArea {
        id: textArea
        x: 100
        y: 452
        width: 1691
        height: 580
        state: ""
        placeholderText: qsTr("prova")
    }

    Text {
        id: text2
        x: 100
        y: 387
        width: 824
        height: 52
        color: "#ffffff"
        text: qsTr("Output Terminal")
        font.pixelSize: 30
        verticalAlignment: Text.AlignVCenter
        font.family: "Verdana"
    }
}
}