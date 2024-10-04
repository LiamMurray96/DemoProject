using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveObject : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }
    public float speed = 5f;

    // Update is called once per frame
    void Update()
    {
      transform.Translate(Pony_cartoon.forward * speed * Time.deltaTime);  
    }
}
