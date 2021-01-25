import QtQuick 2.6
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.2
import QtQuick.Dialogs 1.2

ApplicationWindow {
    id: mainWindow
    title: qsTr("MST Manager")
    width: 1000
    height: 600
    color: "whitesmoke"

    property int standardMargin: 8
    
    onClosing: main.shutdown()

    RowLayout {
	id: mainLayout
	anchors.fill: parent
	
	ColumnLayout {
	    id: buttonColumn
	    spacing: standardMargin
	    Layout.margins: standardMargin

	    Button {
		id: screenA
		text: "Screen A"
		highlighted: main.active_screen_key == "screen_a_key"
		onClicked: main.change_screen("screen_a_key")
	    }

	    Button {
		id: screenB
		text: "Screen B"
		highlighted: main.active_screen_key == "screen_b_key"
		onClicked: main.change_screen("screen_b_key")
	    }

	    Item {
		Layout.fillHeight: true
	    }
	    
	} // buttonColumn

	Loader {
            id: screenLoader
            clip: true

	    Layout.margins: standardMargin
	    Layout.fillHeight: true
	    Layout.fillWidth: true

	    source: main.active_screen_qml_path
	} // screenLoader
	
    } // mainLayout
}
