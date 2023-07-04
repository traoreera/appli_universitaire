import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    width: 400
    height: 300
    visible: true

    Column {
        anchors.centerIn: parent
        spacing: 10

        TextArea {
            id: outputTextArea
            width: parent.width
            height: parent.height - 50
            readOnly: true
            wrapMode: TextEdit.Wrap

            // Affiche la sortie de la ligne de commande
            text: outputText

            // Fait défiler vers le bas automatiquement
            onTextChanged: {
                outputTextArea.cursorPosition = outputTextArea.length
            }
        }

        TextField {
            id: inputTextField
            width: parent.width
            placeholderText: "Entrez une commande"
            onAccepted: {
                // Exécute la commande
                commandRunner.runCommand(inputTextField.text)
                inputTextField.text = ""
            }
        }
    }

    Connections {
        target: commandRunner
        onOutputChanged: {
            // Met à jour la sortie de la ligne de commande
            outputText += output + "\n"
        }
    }

    property string outputText: ""
}
