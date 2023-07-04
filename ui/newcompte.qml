import QtQuick 2.7
import QtQuick.Controls 2.15
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.4
StackView{
    id: info
    initialItem: firstInfo
    anchors.fill: parent

    Component.onCompleted: {
        info.window.source = parent;
    }
    Component{
        id:firstInfo
        Rectangle
        {
            anchors.fill: parent
            color: '#2B2B2B'
            Image{
                source: './ico/panoramique.jpg'
                anchors.fill: parent
                Frame{
                    id:contentHeader
                    x: 0
                    y: 0
                    width: fennetre.width //type: ignore
                    height: 150
                    background: Rectangle{
                        color: '#2B2B2B'
                    }
                }
                Frame{
                    id: contentBody
                    anchors.centerIn: parent
                    background: Rectangle{
                        color: 'transparent'
                        opacity: 0.5
                        radius: 15
                    }
                    width:450
                    Frame{
                        anchors.centerIn: parent
                        background: Rectangle{
                        color: "transparent"
                        }
                        Column{
                            spacing: 20
                            Frame{
                                width: 100
                                height: 100
                                anchors.horizontalCenter: parent.horizontalCenter
                                y: 20
                                background: Rectangle{
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
                                id: nom
                                placeholderText: "nom"
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12
                                background: Rectangle {
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'
                                }
                            }
                            TextField {
                                id: prenom
                                placeholderText: "Prenom"
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12
                                background: Rectangle {
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'
                                }
                            } 
                            TextField {
                                id: codeEtudiant
                                placeholderText: "Code Etudiant"
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12
                                background: Rectangle {
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'
                                }
                            }
                            Button {
                                id: suivant
                                text: "Suivant"
                                anchors.horizontalCenter: parent.horizontalCenter 
                                y: 320
                                width: 100
                                height: 40

                                background: Rectangle {
                                    color: suivant.hovered ? "transparent" : "#940308"
                                    radius: 20
                                    border.width: 1
                                    border.color: "transparent"
                                }

                                contentItem: Text {
                                    text: suivant.text
                                    color: suivant.hovered ? "white" : "white"
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
                                onClicked: info.push(secondInfo)
                            }
                        }
                    }
                }
            }
        }
    }
    Component{
        id: secondInfo
                Rectangle
        {
            anchors.fill: parent
            color: '#2B2B2B'
            Image{
                source: './ico/panoramique.jpg'
                anchors.fill: parent
                Frame{
                    id:contentHeader
                    x: 0
                    y: 0
                    width: fennetre.width //type: ignore
                    height: 150
                    background: Rectangle{
                        color: '#2B2B2B'
                    }
                }
                Frame{
                    id: contentBody
                    anchors.centerIn: parent
                    background: Rectangle{
                        color: 'transparent'
                        opacity: 0.5
                        radius: 15
                    }
                    width:450
                    Frame{
                        anchors.centerIn: parent
                        background: Rectangle{
                        color: "transparent"
                        }
                        Column{
                            spacing: 20
                            Frame{
                                width: 100
                                height: 100
                                anchors.horizontalCenter: parent.horizontalCenter
                                y: 20
                                background: Rectangle{
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
                                id: passwd
                                placeholderText: "mot de passe"
                                echoMode: TextInput.Password
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12
                                background: Rectangle {
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'
                                }
                            }
                            TextField {
                                id: confirmpass
                                placeholderText: "confirme le mot de pass"
                                echoMode: TextInput.Password
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12
                                background: Rectangle {
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'
                                }
                            } 
                            TextField {
                                id: codeEtudiant
                                placeholderText: "Votre Email"
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12
                                background: Rectangle {
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'
                                }
                            }
                            Button {
                                id: inscription
                                text: "Inscription"
                                anchors.horizontalCenter: parent.horizontalCenter 
                                y: 320
                                width: 100
                                height: 40

                                background: Rectangle {
                                    color: inscription.hovered ? "transparent" : "#940308"
                                    radius: 20
                                    border.width: 1
                                    border.color: "transparent"
                                }

                                contentItem: Text {
                                    text: inscription.text
                                    color: inscription.hovered ? "white" : "white"
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

                            }
                        }
                    }
                }
            }
        }
    }
}