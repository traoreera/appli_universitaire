import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle
{
    anchors.fill: parent
    Image

    {
        anchors.fill: parent
        source: "./ico/panoramique.jpg"
        fillMode: Image.PreserveAspectCrop
        Frame
        {
            opacity: 0.5
            id: header
            height: fennetre.height
            width: fennetre.width
            anchors.centerIn: parent

            background: Rectangle { color: 'black'}
        }
        Frame
        {
        width: fennetre.width
        height: 150
        x: 0
        y:-10
        background: Rectangle
        {
        color: '#2B2B2B'
        //radius: 15
        }
        }
    }
    Frame
        {
        anchors.horizontalCenter: parent.horizontalCenter
        y: 200
        width: 450
        height: 300
        opacity: 0.5
        background: Rectangle
        {
        color: '#2B2B2B'
        radius:15
        }

    }
}
