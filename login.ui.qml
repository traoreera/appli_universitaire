import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.4

ApplicationWindow
{
    id: login
    visible: true
    width: 800
    height: 550
    title: qsTr("Login")
    
    Frame
    {
        id: header_frame
        anchors.fill: parent
        width: 100
        height: 10
        
        background: Rectangle{
            color: "gray"
        }
        
        Text{
            text: qsTr('test')
        }
    }
    Text{text: "test"}
}