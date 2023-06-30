import QtQuick 2.7
import QtQuick.Controls 2.15
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.4


Item
{
    function changeColor(){

        if (themes_frame.color =='#001741'){
            drack_mode.running = true; darck_image.running = true;light_text.running = true;}
        else{light_mode.running = true;light_image.running = true;darck_text.running = true;} 
    }

    ColorAnimation {
        id: drack_mode
        target: themes_frame
        property: "color"
        from: '#001741'
        to: '#2B2B2B'
        duration: 2500
        easing.type: Easing.InOutQuad
    }

    ColorAnimation{
        id: light_mode
        target: themes_frame
        property: "color"
        from: '#2B2B2B'
        to: '#001741'
        duration: 2500
        easing.type: Easing.InOutQuad     
    }

    PropertyAnimation{
        id: darck_image
        target: ico_themes
        property: "source"
        from: './ico/darck.png'
        to: './ico/light.png'
        duration: 2500
        easing.type: Easing.InOutQuad
    }


    PropertyAnimation {
        id: light_image
        target: ico_themes
        property: "source"
        from: './ico/light.png'
        to: './ico/darck.png'
        duration: 2500
        easing.type: Easing.InOutQuad
    }


    PropertyAnimation {
        id: light_text
        target: theme_mode
        property: "text"
        from: 'Passer au mode nuit      '
        to: 'Passer au mode jour      '
        duration: 1000
        easing.type: Easing.InOutQuad
    }

    PropertyAnimation{
        id: darck_text
        target: theme_mode
        property: "text"
        from: 'Passer au mode jour      '
        to: 'Passer au mode nuit      '
        duration: 1000
        easing.type: Easing.InOutQuad
    
    }
    Rectangle{
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


            Frame{
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
        Frame{
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

        Button{
            id: theme_mode
            text: "Passer au mode nuit      "
            anchors.bottom: parent.bottom 
            anchors.right: parent.right
            anchors.margins: 10
            font.bold: false
            background:Rectangle{
                border.width: 0
                color: 'transparent'  
                }
            contentItem: Text {
                text: theme_mode.text
                color: "white"
                font.bold: false
                font.pixelSize: 15
                    }
            Image
            {
                id: ico_themes
                source: "./ico/darck.png"
                anchors.right: parent.right
                width: 30
                height: 30
            }
            onClicked:{
                    changeColor();
                }
        }
    }
}