

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
    width: 1080
    height: 720
    title: "Vbite Flasher"
    objectName: "root"
    
Rectangle {
    objectName: "rectangle"
    id: "rectangle"
    width: 1080
    height: 720
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
        anchors.verticalCenterOffset: -302
        anchors.horizontalCenterOffset: 0
        anchors.centerIn: parent
    }

    Image {
        id: favicon
        x: 35
        y: 26
        width: 63
        height: 64
        source: "images/favicon.icns"
        fillMode: Image.PreserveAspectFit
    }

    ComboBox {
        id: combobox
        x: 35
        y: 172
        width: 479
        height: 52
        state: "Seleziona una board..."
        model: devices
        onCurrentTextChanged: comboBoxHandler.selectedItem = currentText
    }

    Text {
        id: text1
        x: 35
        y: 130
        width: 442
        height: 36
        color: "#ffffff"
        text: qsTr("Seleziona la Board per la programmazione:")
        font.pixelSize: 20
        verticalAlignment: Text.AlignVCenter
        font.family: "Verdana"
    }

    Button {
        id: flash_button
        x: 573
        y: 174
        width: 472
        height: 40
        text: qsTr("Flash")
        highlighted: false
        spacing: 8
        font.family: "Verdana"
        icon.source: ""
        flat: false
        icon.color: "#ff7175"
        font.pointSize: 20
        background: Rectangle {
            color: parent.down ? "#88dd66" : (parent.hovered ? "#c57175" : "#ff7175")
            radius: 5
            
        }
        
        onClicked: flashButtonHandler.handleButtonClicked()
    }
    ScrollView{
        x: 35
        y: 298        
        width: 1010
        height: 378
        contentHeight: outputTextArea.height        

        TextArea {
            objectName: "outputTextArea"
            id: outputTextArea
            // x: 35
            // y: 298
            width: 1010
            height: 378
            state: ""
            placeholderText: qsTr("Text Area")
            readOnly: true
        }
    }



    // Connections {
    //     target: commandRunner
    //     function onOutputChanged(output) {
    //         outputTextArea.text = output
    //     }
    // }
    
    Text {
        id: text2
        x: 35
        y: 248
        width: 272
        height: 44
        color: "#ffffff"
        text: qsTr("Output Terminal")
        font.pixelSize: 20
        verticalAlignment: Text.AlignVCenter
        font.family: "Verdana"
    }


}

}