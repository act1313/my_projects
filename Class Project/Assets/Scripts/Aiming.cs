using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Aiming : MonoBehaviour
{
    private float x;
    private float y;
    private Vector3 rotateValue;

    // Update is called once per frame
    void Update()
    {
        y = Input.GetAxis("Mouse X");
        x = Input.GetAxis("Mouse Y");

        Debug.Log(x + ":" + y);

        rotateValue = new Vector3(x, y * -3, 0);
        transform.eulerAngles = transform.eulerAngles - rotateValue;
    }
}
