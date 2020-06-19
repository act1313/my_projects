using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    bool gameHasEnded = false;

    public GameObject enemy;

    private int i = 1;

    public void EndGame()
    {
        if (gameHasEnded == false)
        {
            gameHasEnded = true;
            Invoke("GameEndScreen", 0.0f);
        }
    }

    void GameEndScreen()
    {
        SceneManager.LoadScene("GameOver");
    }

    void Update() 
    {
        if (GameObject.FindWithTag("Enemy") == null)
        {
            SceneManager.LoadScene("WinScreen");
        }
    }
}
