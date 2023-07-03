import QtQuick 2.7
import QtQuick.Controls 2.15
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.4
Item
{ Rectangle{
        anchors.fill: parent
        id: userID
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
                    color: '#001741'
                }
            }
            Frame{
                    id: hemes_frame
                    width: 130
                    height: 130
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 150
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

                StackView{
                    id: stackView
                    initialItem: fennetreLogin
                    width: 200
                    height: 200
                    Component.onCompleted:{
                        stackView.window.source = parent;
                    }
                    Component{
                        id: fennetreLogin
                        Column{
                            anchors.horizontalCenter: parent.horizontalCenter
                            y: 310
                            spacing: 20
                            TextField{
                                id: nom
                                placeholderText: "nom"
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12
                                background: Rectangle{
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'               
                                }
                            }
                            TextField{

                                id: prenom
                                placeholderText: "Prenom"
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12

                                background: Rectangle{
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'    
                                        
                                }
                            }
                            TextField{

                                id: codeEtudiant
                                placeholderText: "Code Etudiant"
                                horizontalAlignment: Text.AlignHCenter
                                width: 330
                                height: 40
                                maximumLength: 40
                                font.bold: true
                                font.pixelSize: 12

                                background: Rectangle{
                                    radius: 20
                                    color: "white"
                                    border.color: 'transparent'    
                                        
                                }
                            }
                        }
                    }
                }
            }
        }
    }