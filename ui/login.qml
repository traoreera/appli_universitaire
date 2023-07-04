import QtQuick 2.7
import QtQuick.Controls 2.15
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.4

Item{
    id: main
    function changeColor() 
            {
                if (themes_frame.color =='#001741'){drack_mode.running = true; darck_image.running = true;light_text.running = true;}
                else{light_mode.running = true;light_image.running = true;darck_text.running = true;} 
            }
            
        Rectangle
        {
            id: themes_frame
            anchors.fill: parent
            color: "#001741"


        ColorAnimation 
            {
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
        PropertyAnimation{

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

        PropertyAnimation {
            id: darck_text
            target: theme_mode
            property: "text"
            from: 'Passer au mode jour      '
            to: 'Passer au mode nuit      '
            duration: 1000
            easing.type: Easing.InOutQuad
        }

            Frame{

                background: Rectangle {
                    color: '#940308'
                }
                width: fennetre.width
                height: 150
                x: 0
                y: 0
            }
            
            Frame{
                id: login_frame_enter
                width: 350
                height: 450
                background:Rectangle
                {
                    radius: 20
                    color: 'transparent'
                }
                
                anchors.horizontalCenter: parent.horizontalCenter
                y:140
                Frame{
                    width: 130
                    height: 130
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 40
                    background: Rectangle
                    {
                        radius: 100
                        color: 'white'
                    }
                    Image{
                        source: "./ico/Icon_user.png"
                        width: 100
                        height: 100
                        anchors.centerIn: parent
                    }
                }
                
                
                
                TextField{

                    id: username
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 200
                    placeholderText: "username"
                    horizontalAlignment: Text.AlignHCenter
                    width: parent.width -20
                    height: 40
                    maximumLength: 40
                    font.pixelSize: 12
                    font.bold: true
                    background: Rectangle{
                        radius: 20
                        color: "white"
                        border.color: 'transparent'    
                    }
                }
                TextField{

                        id: password
                        anchors.horizontalCenter: parent.horizontalCenter 
                        y: 250
                        placeholderText: "password"
                        maximumLength: 30
                        horizontalAlignment: Text.AlignHCenter
                        width: parent.width -20
                        echoMode: TextInput.Password
                        height: 40
                        color: "black"
                        font.bold: true
                        font.pixelSize: 12
                        
                        background: Rectangle
                        {
                            radius: 20
                            color: "white"
                            border.color: 'transparent'    
                        }
                    }
                        
                Button {
                    id: login_bt
                    text: "Connexion"
                    anchors.horizontalCenter: parent.horizontalCenter 
                    y: 320
                    width: 100
                    height: 40

                    background: Rectangle {
                        color: login_bt.hovered ? "transparent" : "#940308"
                        radius: 20
                        border.width: 1
                        border.color: "transparent"
                    }

                    contentItem: Text {
                        text: login_bt.text
                        color: login_bt.hovered ? "white" : "white"
                        font.bold: true
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }

                    onHoveredChanged: {
                        if (hovered) {
                            // Animation pour l'effet de survol
                            background.color = '#720909'
                            contentItem.color = 'white'
                            
                        } else {
                            // Animation pour restaurer l'apparence par défaut
                            background.color = "#940308"
                            contentItem.color = "white"
                            
                        }
                    }

                    onClicked: 
                    {
                        /*
                        scriptRunner.getusername(username.text)   
                        scriptRunner.getpassword(password.text)*/
                    }
                }

                Text{
                    id: new_count

                    text: qsTr("Si vous n'avez pas de pseudo")

                    anchors.horizontalCenter: parent.horizontalCenter 
                    y: 400
                    font.pixelSize: 15
                    
                    color: 'white'
                    opacity: 1
                }

                Button {
                    id: new_compte
                    text: "Inscrivez-vous"
                    font.bold: true
                    font.pixelSize: 20
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 420
                    background: Rectangle
                    {
                        color: 'transparent'
                        border.width: 0
                    }
                    contentItem: Text{

                        text: new_compte.text
                        color: 'white'
                        font.bold: true
                        font.pixelSize: 20
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }


                    onClicked: stackView.push(newCompte)
                }
            }
            Button  {
                id: theme_mode
                text: "Passer au mode nuit      "
                anchors.bottom: parent.bottom 
                anchors.right: parent.right
                anchors.margins: 10
                font.bold: false
                background: Rectangle
                {
                    border.width: 0
                    color: 'transparent'  
                }
                contentItem: Text {
                    text: theme_mode.text
                    color: "white"
                    font.bold: false
                    font.pixelSize: 15
                    }
                Image{

                    id: ico_themes
                    source: "./ico/darck.png"
                    anchors.right: parent.right
                    width: 30
                    height: 30
                    
                    
                }
                onClicked: {changeColor();}
            }
        }
}