pub trait Entity {
    fn increase_health_by(&mut self, amount: usize);
}

struct Player {
    health: usize,
    fire_stamina: usize,
    ice_stamina: usize,
    earth_stamina: usize,
    serum_count: usize,
    super_serum_count: usize,
    stamina_fruit_count: usize,
}

impl Player {
    fn is_alive(&self) -> bool {
        self.health <= 0
    }

    fn reduce_health_by(&mut self, amount: usize) {
        self.health -= amount;
    }

    fn use_serum(&mut self) {
        if self.serum_count > 0 {
            self.health += 10;
            self.serum_count -= 1;
        } else {
            println!("")
        }
    }
}

impl Default for Player {
    fn default() -> Self {
        Self {
            health: 20,
            fire_stamina: 5,
            ice_stamina: 5,
            earth_stamina: 5,
            serum_count: 3,
            super_serum_count: 2,
            stamina_fruit_count: 1,
        }
    }
}

struct Boss {
    frozen: bool,
    health: usize,
}

impl Boss {
    fn is_alive(&self) -> bool {
        self.health <= 0
    }
}

impl Default for Boss {
    fn default() -> Self {
        Self {
            frozen: false,
            health: 100,
        }
    }
}
