using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Enemy : MonoBehaviour
{
    private int deaths = 0;
    // Start is called before the first frame update
    void Start()
    {
        deaths = 0;
    }

    // Update is called once per frame
    void Update()
    {

    }
    void OnCollisionEnter(Collision other) 
    {
        if (other.gameObject.tag == "Bullet")
        {
            Destroy(gameObject);
        }    
    }
}
