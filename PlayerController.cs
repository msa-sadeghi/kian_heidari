using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [Header("movement")]
    public float moveSpeed = 7f;
    [Header("Jump")]
    public float accelerationTimeGrounded = 0.05f;
    public float accelerationTimeAirborne = 0.15f;
    public float jumpHeight = 3f;
    public float timeTojumpApex = 0.35f;

    public float fallMultiplier = 2.5f;
    public float lowJumpMultiplier = 2f;

    public float coyoteTime = 0.12f;
    public float jumpBufferTime = 0.12f;

    public int maxExtraJumps = 1;

    public Transform groundCheck;
    public float groundCheckRadius = 0.12f;
    public LayerMask groundeLayer;

    Rigidbody2D rb;
    Animator animator;
    float horizontalInput;

    float velocityXsmoothing;

    float gravityScaleCalculated;
    float jumpVecolity;
    bool facingRight = true;

    float lastGroundedTime = -10f;
    float lastjumoPressedTime = -10f;
    int extraJumpLeft;

    void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
        animator = GetComponent<Animator>();
        extraJumpLeft = maxExtraJumps;
        CalculatePhysics();
        rb.interpolation = RigidbodyInterpolation2D.Interpolate;
        rb.collisionDetectionMode = CollisionDetectionMode2D.Continuous;
        rb.freezeRotation = true;
    }

    void CalculatePhysics()
    {
        float gravity = (2f * jumpHeight) / (timeTojumpApex * timeTojumpApex);
        gravityScaleCalculated = gravity / Mathf.Abs(Physics2D.gravity.y);

        jumpVecolity = gravity * timeTojumpApex;
    }
    // Start is called before the first frame update

    // Update is called once per frame
    void Update()
    {
        horizontalInput = Input.GetAxisRaw("Horizontal");
        if (Input.GetButtonDown("Jump"))
        {
            lastjumoPressedTime = Time.time;
        }
        // todo change animation
        // todo flip
    }

    void FixedUpdate()
    {
        bool grounded = IsGrounded();
        float targetVelocityX = horizontalInput * moveSpeed;
        float smoothTime = grounded ? accelerationTimeGrounded : accelerationTimeAirborne;
        float newVelX = Mathf.SmoothDamp(rb.velocity.x, targetVelocityX, ref velocityXsmoothing, smoothTime);
        rb.velocity = new Vector2(newVelX, rb.velocity.y);
    }

    bool IsGrounded() {
        Collider2D c = Physics2D.OverlapCircle(groundCheck.position, groundCheckRadius, groundeLayer);
        return c;
    }
}
