from django.db import models


class Skill(models.Model):
    """Skill model for the Jobs and the Candidates"""
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        """Return string representation of the skill"""
        return self.name

class Title(models.Model):
    """Title model for the Jobs and the Candidates"""
    name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        """Return string representation of the title"""
        return self.name

class Candidate(models.Model):
    """Database model for Candidates in the system"""
    name = models.CharField(max_length=255,unique=True) 
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

    def get_full_name(self):
        """Retrieve full name of candidate"""
        return self.name


    def __str__(self):
        """Return string representation of the candidate"""
        return self.name 


class Job(models.Model):
    """Database model for Jobs in the system"""

    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        """Return string representation of the job"""
        return self.title.name

