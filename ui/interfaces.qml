import QtQuick 2.7
import QtQuick.Controls 2.15
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.4

// fenetre principale
ApplicationWindow {

    id: fennetre
    visible: true
    minimumWidth: 900
    minimumHeight: 650
    title: qsTr("Login")
    
    
    StackView {
        /*
            stack view permet de change de fennetre en fonction de du login ou de la creation de compte
            
        */
        id: stackView
        initialItem: fennetreLogin
        anchors.fill: parent
        Component.onCompleted: 
        {
            stackView.window.source = parent;
        }
        
        Component
        {
            id: fennetreLogin
            Loader
            {
                source: './login.qml'
            }
        }
        Component{
            id: newCompte

            Loader
            {
                source: './newcompte.qml'
            }
        }
            
    }
}