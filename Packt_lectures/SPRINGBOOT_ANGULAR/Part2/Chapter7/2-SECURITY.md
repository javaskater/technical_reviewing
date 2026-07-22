# [Extending WebSecurityConfigurerAdapter](https://github.com/PacktPublishing/Spring-Boot-and-Angular/blob/main/Chapter-07/superheroes/src/main/java/com/example/springbootsuperheroes/superheroes/config/SecurityConfig.java)

# 139

# Tree @Overriden methods

## Two times calling configure method

### one for setting the authentifier

- with The [ApplicationUserDetailsService userDetailsService](https://github.com/PacktPublishing/Spring-Boot-and-Angular/blob/main/Chapter-07/superheroes/src/main/java/com/example/springbootsuperheroes/superheroes/jwt/services/ApplicationUserDetailsService.java)

### More on the UserService

- the only necessary and overriden method is **loadUserByUsername** (here the username is the email)
- the authenticate method is directly called by the AuthenticationController

```bash
jmena01@m077-2281091:~/Ateliers/intellj/idea-IU-261.25134.95/workspace/superheroes/src/main/java/com/example/springbootsuperheroes/superheroes$ grep -rn authenticate .
./jwt/services/ApplicationUserDetailsService.java:29:  public UserEntity authenticate(String email, String password)
./jwt/controllers/AuthenticateController.java:25:  @RequestMapping(value = "/authenticate") #used directly by the controller and only there
./jwt/controllers/AuthenticateController.java:27:  public AuthenticationResponse authenticate(
./jwt/controllers/AuthenticateController.java:33:      user = userDetailsService.authenticate(req.getEmail(), req.getPassword());
```

### The other for the http chain of auhorizations

- it is the very classical chain of authorizations in SpringSecurity

## Remarks

- in the Controller we don't use the authenticationManager we defined in the SercurityConfig
  - instead we use directly the authenticate method of userDetailsService
- [jwt](https://en.wikipedia.org/wiki/JSON_Web_Token)
  - a very good [Blog Article (in french sorry)](https://blog.ippon.fr/2017/10/12/preuve-dauthentification-avec-jwt/)
    - explaining also how it is used in Spring (TO READ)
  - used in [util/JwtUtil](https://github.com/PacktPublishing/Spring-Boot-and-Angular/blob/main/Chapter-07/superheroes/src/main/java/com/example/springbootsuperheroes/superheroes/jwt/util/JwtUtil.java)
  - it is added to the Response when we authenticate
