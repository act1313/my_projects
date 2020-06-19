using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class StartOver : MonoBehaviour
{
    public void StartOverNow()
    {
        SceneManager.LoadScene("Game");
    }
}
