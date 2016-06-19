from django.db import models


class BigFish(models.Model):
    BASS = 1
    CRAPPIE = 2
    NORTHERN = 3
    WALLEYE = 4
    SPECIES = (
        (BASS, "Bass"),
        (CRAPPIE, "Crappie"),
        (NORTHERN, "Northern"),
        (WALLEYE, "Walleye"),
    )
    year = models.ForeignKey('Year', related_name="big_fish")
    species = models.IntegerField(choices=SPECIES, default=NORTHERN)
    length = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        string = "{0}lb. {1}\" {2}"
        species = self.SPECIES[self.species - 1][1]
        return string.format(self.weight, self.length, species)

    class Meta:
        verbose_name_plural = "Big fish"


class Day(models.Model):
    SATURDAY = 1
    SUNDAY = 2
    MONDAY = 3
    TUESDAY = 4
    WEDNESDAY = 5
    THURSDAY = 6
    FRIDAY = 7
    DAYS = (
        (SATURDAY, "Saturday"),
        (SUNDAY, "Sunday"),
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
    )
    day = models.IntegerField(choices=DAYS)
    year = models.ForeignKey('Year', related_name="days")
    bass = models.IntegerField(default=0)
    crappie = models.IntegerField(default=0)
    northern = models.IntegerField(default=0)
    walleye = models.IntegerField(default=0)

    def __str__(self):
        return "{0} {1}".format(self.day, self.year)

    @property
    def total(self):
        return self.bass + self.crappie + self.northern + self.walleye


class Year(models.Model):
    year = models.IntegerField(unique=True, db_index=True)

    def __str__(self):
        return str(self.year)

    @property
    def big_bass(self):
        return self.big_fish.filter(species=BigFish.BASS)

    @property
    def big_northern(self):
        return self.big_fish.filter(species=BigFish.NORTHERN)

    @property
    def big_walleye(self):
        return self.big_fish.filter(species=BigFish.WALLEYE)

    @property
    def bass(self):
        return [(n.weight, n.length) for n in self.big_bass]

    @property
    def northern(self):
        return [(n.weight, n.length) for n in self.big_northern]

    @property
    def walleye(self):
        return [(n.weight, n.length) for n in self.big_walleye]
