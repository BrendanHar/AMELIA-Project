using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;


public class menuControl : MonoBehaviour
{
    public TMP_Text colorText;
    public TMP_Text sizeText;
    public TMP_Text shapeText;
    public TMP_Text actionText;
    public GameObject confirmMenu;
    public GameObject mainMenu;
    
    private bool colorSet = false;
    private bool sizeSet = false;
    private bool shapeSet = false;
    private bool actionSet = false;
    private string color;
    private string action;
    private string shape;
    private string size;
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // confirmSelection();
    }
    // TODO: build a target object that takes all of the current parameters and builds a tuple with color, size, shape, and action
    // Then send that over socket connection to the computer in question
    public void Select_Color(string color){
        if (color == "blue"){
            colorText.text = "Selected: Blue";
            colorSet = true;
            Debug.Log("selected blue");
        } else if (color == "green"){
            colorText.text = "Selected: Green";
            colorSet = true;
            Debug.Log("selected green");
        } else if (color == "red"){
            colorText.text = "Selected: Red";
            colorSet = true;
            Debug.Log("selected Red");
        } else if (color == "yellow"){
            colorText.text = "Selected: Yellow";
            colorSet = true;
            Debug.Log("selected Yellow");
        }
    }

    public void ResetMenu(){
        colorSet = false;
        actionSet = false;
        sizeSet = false;
        shapeSet = false;
        colorText.text = "Select Color";
        sizeText.text = "Select Size";
        shapeText.text = "Select Shape";
        actionText.text = "Select Action";
    }

    public void Select_Action(string action){
        if (action == "bin"){
            actionText.text = "Destination: Bin";
            actionSet = true;
            Debug.Log("Place Item in bin");
        } else if (action == "hand"){
            actionText.text = "Destination: Hand";
            actionSet = true;
            Debug.Log("Hand Item to User");
        }
    }

    public void confirmSelection(){
        if (colorSet && actionSet && sizeSet && shapeSet){
            Debug.Log("got confirm menu");
            // confirmMenu.SetActive(true);
            mainMenu.SetActive(false);
        }
    }

    public void Select_Size(string size){
        if (size == "large"){
            sizeText.text = "Selected: Large";
            sizeSet = true;
            Debug.Log("Large");
        } else if (size =="small"){
            sizeText.text = "Selected: Small";
            sizeSet = true;
            Debug.Log("Small");
        }
    }

    public void Select_Shape(string shape){
        if (shape == "cube"){
            shapeText.text = "Selected: Cube";
            shapeSet = true;
            Debug.Log("Cube");
        } else if (shape == "cylinder"){
            shapeText.text = "Selected: Cylinder";
            shapeSet = true;
            Debug.Log("Cylinder");
        }
    }



}
