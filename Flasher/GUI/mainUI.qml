

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5 // 2.15?
import QtQuick.Layouts 1.15

ApplicationWindow{
    id: mainWindow
    visible: true
    width: 1080
    height: 720
    minimumWidth: 600
    minimumHeight: 600
    title: "Vbite Flasher"
    objectName: "root"
    onClosing: handleClose.handle_close()
    
    Rectangle {
        objectName: "rectangle"
        id: rectangle
        width: parent.width
        height: parent.height
        color: "#0c1012"
        radius: 0
        Column {
            id: mainColumn
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.topMargin: 25
            anchors.leftMargin: 35
            anchors.rightMargin: 35
            anchors.bottomMargin: 25
            spacing: 15
            Row {
                id: topRow
                x: 0
                width: parent.width
                anchors.top: parent.top
                bottomPadding: 15
                topPadding: 0
                anchors.topMargin: 0
                height: Math.max(favicon.height, title.height)
                Image {
                    id: favicon
                    width: 64
                    height: 64
                    anchors.left: parent.left
                    anchors.top: parent.top
                    source: "images/favicon.ico"
                    anchors.topMargin: 0
                    anchors.leftMargin: 0
                    fillMode: Image.PreserveAspectFit
                }
                Text {
                    id: title
                    height: 54
                    color: "#ffffff"
                    text: qsTr("Vbite Flasher")
                    font.family: "Verdana"
                    font.pointSize: 42
                    minimumPixelSize: 19
                    minimumPointSize: 27
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }

            Row {
                id: middleRow
                x: 0
                width: parent.width
                height: Math.max(comboCol.height, flash_button.height)
                anchors.top: topRow.bottom
                spacing: 15
                anchors.topMargin: 0
                Column {
                    id: comboCol
                    rightPadding: 10
                    width: parent.width / 2
                    Text {
                        id: textCombo
                        x: 0
                        y: 130
                        width: parent.width / 2 - 10
                        height: 36
                        color: "#ffffff"
                        text: qsTr("Seleziona la Board per la programmazione:")
                        font.pixelSize: 20
                        verticalAlignment: Text.AlignVCenter
                        font.family: "Verdana"
                    }
                    ComboBox {
                        id: combobox
                        objectName: "ComboBox"
                        x: 0
                        y: 172
                        width: parent.width - 10
                        height: 52
                        opacity: 1
                        scale: 1
                        // PlaceholderText: "Seleziona una Board..."
                        state: "Seleziona una board..."
                        model: devices
                        currentIndex: -1
                        displayText: currentIndex === -1 ? "Seleziona una Board..." : currentText
                        
                        onCurrentTextChanged: comboBoxHandler.selectedItem = currentText
                        onCurrentIndexChanged: comboBoxHandler.selectedItem = currentText
                    }
                }

                Button {
                    id: flash_button
                    x: 573 - 35
                    y: 174
                    anchors.bottom: parent.bottom
                    leftPadding: 31
                    anchors.rightMargin: 0
                    width: middleRow.width / 2 - 10
                    height: combobox.height
                    text: qsTr("Flash")
                    anchors.right: parent.right
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
            }

            Column {
                id: bottomColumn
                anchors.top: middleRow.bottom
                anchors.right: parent.right
                anchors.left: parent.left
                anchors.bottom: parent.bottom
                topPadding: 15
                Text {
                    id: text2
                    x: 0
                    height: 44
                    color: "#ffffff"
                    text: qsTr("Output Terminal")
                    anchors.top: parent.top
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignVCenter
                    anchors.topMargin: 0
                    font.family: "Verdana"
                }

                ScrollView {
                    id: scrollView
                    x: outputTextArea.x
                    width: parent.width
                    anchors.top: text2.bottom
                    anchors.topMargin: 0
                    anchors.left: parent.left
                    // contentHeight: outputTextArea.height - 10
                    contentHeight: bottomColumn.height - text2.height

                    TextArea {
                        objectName: "outputTextArea"
                        id: outputTextArea
                        width: parent.width
                        height: bottomColumn.height - text2.height
                        anchors.left: parent.left
                        anchors.top: text2.bottom
                        anchors.leftMargin: 0
                        anchors.topMargin: -20
                        state: ""
                        placeholderText: qsTr("Text Area")
                        readOnly: true
                    }
                }
            }
        }
    } 
    // function handleClose() {
    //     Qt.quit() // This will close the GUI
    // }
}
