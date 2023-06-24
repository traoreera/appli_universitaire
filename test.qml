import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Switch avec deux interfaces"

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: page1 // Page initiale

        Component.onCompleted: {
            // Définir la fenêtre source pour les transitions
            stackView.window.source = parent;
        }

        // Première page
        Component {
            id: page1
            Rectangle {
                width: parent.width
                height: parent.height
                color: "lightblue"

                Button {
                    anchors.centerIn: parent
                    text: "Passer à la page 2"
                    onClicked: stackView.push(page2)
                }
            }
        }

        // Deuxième page
        Component {
            id: page2
            Rectangle {
                width: parent.width
                height: parent.height
                color: "lightgreen"

                Button {
                    anchors.centerIn: parent
                    text: "Revenir à la page 1"
                    onClicked: stackView.pop()
                }
            }
        }
    }
}
